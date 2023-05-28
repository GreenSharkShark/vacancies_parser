import requests


class HHAreaFinder:
    """
    API hh.ru в посзволяет в ответ на запрос города для поиска получить список с точными возможными локациями для поиска.
    Именно для этого нужен этот класс. API сайта SuperJob так делать не позволяет, по этому для него такого класса нет.
    """
    def __init__(self, desired_location):
        self.place = {}
        self.desired_location = desired_location
        self.url = "https://api.hh.ru/suggests/areas"

    def __get_area(self):
        response = requests.get(self.url, params={'text': self.desired_location}).json()
        return response

    def process_response(self):
        data = self.__get_area()
        try:
            if len(data['items']) == 1:
                return data['items'][0]['id']
        except KeyError:
            return '1'

        counter = 1
        for i in data['items']:
            region = f"{counter} {i['text']}"
            self.place[region] = i['id']
            counter += 1
            print(region)
        answer = input('Уточните регион поиска. Введите номер интересующего вас региона: ')
        if not int(answer):
            raise ValueError('Введенное значение должно быть числом.')
        for i in self.place.keys():
            if int(answer) == int(i[0]):
                return self.place.get(i)
