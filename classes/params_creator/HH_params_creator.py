from classes.params_creator.ABC_params_creator import ABCParamsCreator


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

        if int(period) > 0:
            self.headers['period'] = str(period)

        self.headers["per_page"] = "100"
        return self.headers
