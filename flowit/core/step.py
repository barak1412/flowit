from abc import abstractmethod
from flowit.core.runnable_component import IRunnableComponent


class IStep(IRunnableComponent):
    def __init__(self, name: str = None):
        super().__init__(name=name)

    @abstractmethod
    def process(self, *args, **kwargs):
        pass

