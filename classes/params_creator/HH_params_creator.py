from classes.params_creator.ABC_params_creator import ABCParamsCreator


class HHParamsCreator(ABCParamsCreator):
    def __init__(self):
        self.headers = {}

    def create_params(self, search_query, period, place):
        self.headers["text"] = search_query

        self.headers["area"] = place

        self.headers['period'] = str(period)

        self.headers["per_page"] = "100"
        return self.headers
