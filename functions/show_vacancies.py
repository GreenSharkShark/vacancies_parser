from classes.json_processor.json_processor import JSONProcessor
from functions.get_help import get_help


def show_vacancies(vacancies_list_objects):
    json_saver = JSONProcessor()
    for index, value in enumerate(vacancies_list_objects):
        print(f'{index}: {value}')
    while True:
        answer = input('Режим просмотра вакансий: ').lower()
        if answer.split()[0] == 'сохранить':
            _index = int(answer.split()[1])
            json_saver.save_to_favorites(vacancies_list_objects[_index])
            print('Сохранено.')
        elif answer == 'назад':
            break
        elif answer == 'выход':
            quit()
        elif answer == 'получить помощь':
            get_help()
        else:
            print(answer, 'не является внутренней командой.')
