from abc import ABC, abstractmethod


class IRunnableComponent(ABC):
    @abstractmethod
    def process(self, *args, **kwargs):
        pass
