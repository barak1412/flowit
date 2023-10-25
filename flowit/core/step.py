from abc import abstractmethod
from flowit.core.runnable_component import IRunnableComponent


class IStep(IRunnableComponent):
    @abstractmethod
    def process(self, *args, **kwargs):
        pass

