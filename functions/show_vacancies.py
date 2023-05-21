from classes.json_processor.json_processor import JSONProcessor
from functions.get_help import get_help


def show_vacancies(vacancies_list_objects):
    json_saver = JSONProcessor()
    first_iteration = True
    while True:
        for i in vacancies_list_objects:
            if first_iteration:
                print(i)
                first_iteration = False
            answer = input('Режим просмотра вакансий: ').lower()
            if answer == 'дальше':
                print(i)
            elif answer == 'сохранить':
                json_saver.save_to_favorites(i)
                print('Сохранено.')
            elif answer == 'назад':
                break
            elif answer == 'выход':
                quit()
            elif answer == 'получить помощь':
                get_help()
            else:
                print(answer, 'не является внутренней командой.')
        break
