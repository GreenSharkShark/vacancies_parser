from classes.area_finder.ABC_area_finder import AreaFinder
import os


import requests


class SJAreaFinder(AreaFinder):
    def __init__(self, desired_location):
        self.url = 'https://api.superjob.ru/2.0/regions/combined/'
        self.desired_location = {"town": desired_location}
        self.headers = {"X-Api-App-Id": os.environ.get('SJAPI')}

    def get_area(self):
        response = requests.get(self.url, headers=self.headers)
        return response.text

    def process_response(self):
        pass


a = SJAreaFinder('Екатеринбург')
print(a.get_area())