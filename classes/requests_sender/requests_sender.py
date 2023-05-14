from abc import ABC, abstractmethod


class RequestsSender(ABC):

    @abstractmethod
    def find_vacancies(self):
        pass
