from classes.area_finder import AreaFinder


class ParamsCreator:
    def __init__(self):
        self.headers = {}

    def create_params(self, search_query, period, place):
        self.headers["text"] = search_query

        self.headers["area"] = place

        self.headers['period'] = str(period)

        self.headers["per_page"] = "100"
        return self.headers
