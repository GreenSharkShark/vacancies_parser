class Vacancy:
    def __init__(self, name, salary, url, description, place):
        self.__name = name
        self.__salary = salary if salary else 'ЗП не указана'
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
                salary = i['salary']
            except KeyError:
                salary = 'Не найдено'

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
            objects_list.append(cls(name, salary, url, description, place))

        for i in sj_response['objects']:
            try:
                name = i['profession']
            except KeyError:
                name = 'Не найдено'

            try:
                salary = i['payment_from']
            except KeyError:
                salary = 'Не найдено'

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
            objects_list.append(cls(name, salary, url, description, place))

        return objects_list

    def __str__(self):
        return f'{self.__name}\n' \
               f'{self.__place}\n' \
               f'{self.__description}\n' \
               f'{self.__url}\n' \
               f'{self.__salary}'
