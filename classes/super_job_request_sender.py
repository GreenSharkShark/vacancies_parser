import os
from classes.requests_sender import RequestsSender


import requests


class SuperJobRequestsSender(RequestsSender):
    def __init__(self, params):
        self.url = 'https://api.superjob.ru/2.33/vacancies/'
        self.headers = os.environ.get('SuperJob_API')
        self.params = params

    def find_vacancies(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.text
