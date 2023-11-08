from abc import ABC, abstractmethod


class IRunnableComponent(ABC):
    def __init__(self, name: str = None):
        if name is None:
            self._name = self.__class__.__name__
        else:
            self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def process(self, *args, **kwargs):
        pass
