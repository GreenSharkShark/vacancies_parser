from classes.area_finder.HHarea_finder import HHAreaFinder
from classes.params_creator.SJ_params_creator import SJParamsCreator
from classes.params_creator.HH_params_creator import HHParamsCreator
from classes.requests_sender.super_job_request_sender import SuperJobRequestsSender
from classes.requests_sender.hh_requests_sender import HunterRequestsSender
from classes.json_processor.json_processor import JSONProcessor
from classes.vacancy.vacancy import Vacancy
from functions.show_vacancies import show_vacancies
from functions.show_favorites import show_favorites


def run_search():
    search_query = str(input('Введите поисковый запрос: '))
    period = str(input(f'Введите период времени за который хотите получить результаты:\n'
                       f'0 - за все время.\n'
                       f'1 - за последний день.\n'
                       f'3 - за последние 3 дня.\n'
                       f'30 - за последний месяц.\n'
                       f'60 - за последние 2 месяца.\n'
                       f'90 - за последние 3 месяца.\n'))
    place = str(input('Введите город для поиска: '))
    hh_place = HHAreaFinder(place).process_response()

    hh_params = HHParamsCreator().create_params(search_query, period, hh_place)
    sj_params = SJParamsCreator().create_params(search_query, period, place)

    hh_response = HunterRequestsSender(hh_params).find_vacancies()
    sj_response = SuperJobRequestsSender(sj_params).find_vacancies()

    json_saver = JSONProcessor()
    json_saver.save_to_json(hh_response, 'hh')
    json_saver.save_to_json(sj_response, 'sj')
    vacancies = Vacancy.make_objects(hh_response, sj_response)
    return vacancies


def main_menu():
    while True:
        answer = input('Главное меню: ')
        if answer.lower() == 'поиск':
            vacancies = run_search()
            show_vacancies(vacancies)
        elif answer.lower() == 'просмотреть сохраненные':
            show_favorites()
        elif answer.lower() == 'выход':
            print('Досвидули.')
            quit()
        else:
            print(answer, 'не является внутренней командой.')


if __name__ == '__main__':
    main_menu()
