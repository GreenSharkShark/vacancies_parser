from dotenv import load_dotenv
import os
from classes.requests_sender.requests_sender import RequestsSender

import requests


load_dotenv()

#  тут комментарии излишни


class SuperJobRequestsSender(RequestsSender):
    def __init__(self, params):
        self.url = 'https://api.superjob.ru/2.33/vacancies/'
        self.headers = {"X-Api-App-Id": os.environ.get('SJAPI')}
        self.params = params

    def find_vacancies(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        response.encoding = 'utf-8'
        return response.json()
