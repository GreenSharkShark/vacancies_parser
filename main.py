from classes.hh_requests_sender import HunterRequestsSender
from classes.area_finder import AreaFinder
from classes.params_creator_for_request import ParamsCreator


place = input('Введите регион для поиска вакансий: ')
place_id = AreaFinder(place).process_response()

search_query = str(input('Введите название вакансии: '))
period = input('Введите период в днях за который хотите получить результаты: ')

params = ParamsCreator().create_params(search_query, period, place_id)

vacancies = HunterRequestsSender(params)
print(vacancies.find_vacancies())
