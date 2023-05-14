from classes.requests_sender.requests_sender import RequestsSender


import requests


class HunterRequestsSender(RequestsSender):
    def __init__(self, params):
        self.url = "https://api.hh.ru/vacancies"
        self.params = params

    def find_vacancies(self):
        request = requests.get(self.url, params=self.params)
        return request.text
