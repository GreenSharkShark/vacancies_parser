from classes.params_creator.ABC_params_creator import ABCParamsCreator


class SJParamsCreator(ABCParamsCreator):
    def __init__(self):
        self.params = {}

    def create_params(self, search_query, period, place):
        self.params["keyword"] = str(search_query)

        self.params["town"] = str(place)

        self.params["period"] = str(period)

        self.params["count"] = "1000"  # Количество объектов в ответе. Макс 1000
        return self.params

    def __str__(self):
        return ' '.join(self.params)
