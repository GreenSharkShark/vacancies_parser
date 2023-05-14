from abc import ABC, abstractmethod


class AreaFinder(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def process_response(self):
        pass
