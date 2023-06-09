from abc import ABC, abstractmethod


class ABCParamsCreator(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_params(self, search_query, period, place):
        pass


class HHParamsCreator(ABCParamsCreator):
    """
    Создает словарь с базовыми параметрами для поиска. Раз уж API позволяет получить не все вакансии сразу,
    а только те, что меня интересуют, я решил этим воспользоваться. Просто чтобы потом не перебирать в цикле
    сотни или тысячи вакансий чтобынайти только нужный мне город.
    """
    def __init__(self):
        self.headers = {}

    def create_params(self, search_query, period, place):
        self.headers["text"] = search_query

        self.headers["area"] = place

        try:
            if int(period) > 0:
                self.headers['period'] = str(period)
        except ValueError:
            pass  # Если ввели неверное значение ключ 'period' не передается и возвращаются пезультаты за все время

        self.headers["per_page"] = "100"
        return self.headers


class SJParamsCreator(ABCParamsCreator):
    """
        Создает словарь с базовыми параметрами для поиска. Раз уж API позволяет получить не все вакансии сразу,
        а только те, что меня интересуют, я решил этим воспользоваться. Просто чтобы потом не перебирать в цикле
        сотни или тысячи вакансий чтобынайти только нужный мне город.
    """
    def __init__(self):
        self.params = {}

    def create_params(self, search_query, period, place):
        self.params["keyword"] = str(search_query)

        self.params["town"] = str(place)

        self.params["period"] = str(period)

        self.params["count"] = "1000"  # Количество объектов в ответе. Макс 1000

        self.params["Accept-Charset"] = 'utf-8'
        return self.params

    def __str__(self):
        return ' '.join(self.params)
