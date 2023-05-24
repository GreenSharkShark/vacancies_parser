class Vacancy:
    def __init__(self, name, url, description, place, salary_from=None, salary_to=None):
        self.__name = name
        self._salary_from = int(salary_from) if salary_from else None
        self._salary_to = int(salary_to) if salary_to else None
        self.__url = url
        self.__description = description
        self.__place = place

    @classmethod
    def make_objects(cls, hh_response, sj_response):
        """
        Классметод для создания списка экземпляров класса
        :param hh_response:
        :param sj_response:
        :return:
        """
        objects_list = []
        for i in hh_response['items']:
            try:
                name = i['name']
            except KeyError:
                name = 'Не найдено'

            try:
                salary_from = i['salary']['from']
            except (KeyError, TypeError):
                salary_from = None

            try:
                salary_to = i['salary']['from']
            except (KeyError, TypeError):
                salary_to = None

            try:
                url = i['alternate_url']
            except KeyError:
                url = 'Не найдено'

            try:
                description = i['snippet']['requirement']
            except KeyError:
                description = 'Не найдено'

            try:
                place = i['area']['name']
            except KeyError:
                place = 'Не найдено'
            objects_list.append(cls(name, url, description, place, salary_from, salary_to))

        for i in sj_response['objects']:
            try:
                name = i['profession']
            except KeyError:
                name = 'Не найдено'

            try:
                salary_from = i['payment_from']
            except KeyError:
                salary_from = 'Не найдено'

            try:
                salary_to = i['payment_to']
            except KeyError:
                salary_to = 'Не найдено'

            try:
                url = i['client']['link']
            except KeyError:
                url = 'Не найдено'

            try:
                description = i['candidat']
            except KeyError:
                description = 'Не найдено'

            try:
                place = i['client']['town']['title']
            except KeyError:
                place = 'Не найдено'
            objects_list.append(cls(name, url, description, place, salary_from, salary_to))

        return objects_list

    def __str__(self):
        if self._salary_to:
            salary = f'ЗП от {self._salary_from} до {self._salary_to}.'
        else:
            salary = f'ЗП от {self._salary_from}.'
        return f'{self.__name}\n' \
               f'{self.__place}\n' \
               f'{self.__description}\n' \
               f'{self.__url}\n' \
               f'{salary}'
