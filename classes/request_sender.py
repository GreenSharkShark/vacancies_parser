from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os

import requests


load_dotenv()


class RequestsSender(ABC):

    @abstractmethod
    def find_vacancies(self):
        pass


class SuperJobRequestsSender(RequestsSender):
    def __init__(self, params):
        self.url = 'https://api.superjob.ru/2.33/vacancies/'
        self.headers = {"X-Api-App-Id": os.environ.get('SJAPI')}
        self.params = params

    def find_vacancies(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        response.encoding = 'utf-8'
        return response.json()


class HunterRequestsSender(RequestsSender):
    def __init__(self, params):
        self.url = "https://api.hh.ru/vacancies"
        self.params = params

    def find_vacancies(self):
        request = requests.get(self.url, params=self.params)
        return request.json()
