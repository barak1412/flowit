import networkx as nx
from typing import Dict
from flowit.core.runnable_component import IRunnableComponent


class Workflow(IRunnableComponent):
    def __init__(self, name: str = None):
        super().__init__(name=name)

        self._components_dag = nx.DiGraph()
        self._components_required_inputs = {}
        self._components_outputs = {}
        self._output_component = None

    def add_link(self, src_component: IRunnableComponent, dst_component: IRunnableComponent,
                 params_mapping: Dict[str, str]):
        self._components_dag.add_edge(src_component, dst_component)
        if dst_component not in self._components_required_inputs:
            self._components_required_inputs[dst_component] = {}
        self._components_required_inputs[dst_component][src_component] = params_mapping

    def set_output_component(self, runnable_component):
        if not self._components_dag.has_node(runnable_component):
            raise Exception('You may not set a node that does not exist in graph')
        self._output_component = runnable_component

    def process(self, *args, **kwargs):
        # verify DAG
        if not nx.is_directed_acyclic_graph(self._components_dag):
            raise Exception('Workflow must be directed acyclic graph.')

        # sort nodes according to topological order
        ordered_nodes = [n for n in nx.topological_sort(self._components_dag)]

        # run every node with its desired inputs
        for node in ordered_nodes:
            if node not in self._components_required_inputs:
                node_outputs = node.process()
            else:
                input_dict = {}
                for pre_node in self._components_required_inputs[node]:
                    for pre_node_output in self._components_required_inputs[node][pre_node]:
                        param_name = self._components_required_inputs[node][pre_node][pre_node_output]
                        param_value = self._components_outputs[pre_node][pre_node_output]
                        input_dict[param_name] = param_value
                node_outputs = node.process(**input_dict)
            self._components_outputs[node] = node_outputs
        if self._output_component is not None:
            return self._components_outputs[self._output_component]
        return None
