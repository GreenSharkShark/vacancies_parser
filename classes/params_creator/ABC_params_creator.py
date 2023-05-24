from abc import ABC, abstractmethod


class ABCParamsCreator(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_params(self, search_query, period, place):
        pass
