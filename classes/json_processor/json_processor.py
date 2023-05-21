import json
import os
import datetime
from classes.vacancy.vacancy import Vacancy


class JSONProcessor:
    """
    Класс для чтения и записи json файлов.
    """

    def __init__(self):
        self.__hh_file_path = '/home/purple_rabbit/coursepaper4/json_responses/hh_response_logs.json'
        self.__sj_file_path = '/home/purple_rabbit/coursepaper4/json_responses/sj_response_logs.json'
        self.__fav_file_path = '/home/purple_rabbit/coursepaper4/json_responses/favorite.json'

    def __return_filepath(self, filename):
        if filename == 'hh':
            file_path = self.__hh_file_path
        elif filename == 'sj':
            file_path = self.__sj_file_path
        elif filename == 'fav':
            file_path = self.__fav_file_path
        return file_path

    def __open_and_return_content(self, filename):
        """
        Метод для проверки наличия содержимого в файлах
        :param filename:
        :return:
        """
        file_path = self.__return_filepath(filename)
        with open(file_path) as file:
            content = json.load(file)
        return content if content else False

    @staticmethod
    def __open_and_write(file_path, content):
        """
        Метод для открытия файла и записи в него переданных данных
        :param file_path:
        :param content:
        :return:
        """
        with open(file_path, 'w') as file:
            json.dump(content, file)

    def __is_file(self, filename):
        """
        Метод для проверки создани ли уже нужный файл
        :param filename:
        :return:
        """
        file_path = self.__return_filepath(filename)
        return True if os.path.isfile(file_path) else False

    def save_to_json(self, data, filename):
        """
        Метод принимает на вход донные и записывает их в файл в виде json словаря, где ключом является текущая дата и время,
        а значением принимаемые на вход данные. Эти данные мне лично не очень-то и нужны, но в принципе их можно использовать
        для какого-либо анализа.
        :param data:
        :param filename:
        :return:
        """
        file_path = self.__return_filepath(filename)
        if self.__is_file(filename):  # Проверяем существует ли файл

            content = self.__open_and_return_content(filename)  # Проверяем не пустой ли файл
            if content is True:
                content[str(datetime.datetime.now())] = [data]
            else:
                content = {str(datetime.datetime.now()): [data]}

            self.__open_and_write(file_path, content)
        else:
            content = {str(datetime.datetime.now()): [data]}
            self.__open_and_write(file_path, content)

    def save_to_favorites(self, objects):
        """
        Метод для сохранения вакансий в избранное.
        :param objects: Объект вакансии который нужно сохранить
        :return: None
        """
        file_path = self.__fav_file_path
        if os.path.isfile(file_path):  # Проверяем существует ли файл
            content = self.__open_and_return_content('fav')
            if content:
                content.append(objects.__dict__)
            else:
                content = [objects.__dict__]
            self.__open_and_write(file_path, content)
        else:
            content = [objects.__dict__]
            self.__open_and_write(file_path, content)

    def remove_from_favorites(self):
        pass

    def show_favorites(self):
        """
        Метод для чтения данных ис файла с сохраненными вакансиями.
        :return: error if error else objects_list
        """
        try:
            objects = self.__open_and_return_content('fav')
        except FileNotFoundError:
            return 'error'
        objects_list = []
        for i in objects:
            name = i['_Vacancy__name']
            salary = i['_Vacancy__salary']
            url = i['_Vacancy__url']
            description = i['_Vacancy__description']
            place = i['_Vacancy__place']
            objects_list.append(Vacancy(name, salary, url, description, place))
        return objects_list
