from classes.requests_sender.super_job_request_sender import SuperJobRequestsSender
from classes.params_creator.SJ_params_creator import SJParamsCreator


search_query = str(input('Поисковый запрос: '))
period = str(input(f'Период:\n'
                   f'0 Все вакансии\n'
                   f'1 За последний день\n'
                   f'3 За последние 3 дня\n'
                   f'7 За неделю\n'
                   f'30 За месяц\n'
                   f'60 За последни 3 месяца\n'
                   f'90 За последние 6 месяцев\n'))
place = str(input('Место поиска: '))

sj = SJParamsCreator()
a = sj.create_params(search_query, period, place)
sj_vacancies = SuperJobRequestsSender(a)
print(sj_vacancies.find_vacancies())
