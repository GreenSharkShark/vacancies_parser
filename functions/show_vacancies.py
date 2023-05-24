from classes.json_processor.json_processor import JSONProcessor
from functions.get_help import get_help


def show_vacancies(vacancies_list_objects):
    json_saver = JSONProcessor()
    for index, value in enumerate(vacancies_list_objects):
        print(f'{index}: {value}')
    while True:
        answer = input('Режим просмотра вакансий: ').lower().split()
        if answer[0] == 'сохранить':
            _index = int(answer[1])
            json_saver.save_to_favorites(vacancies_list_objects[_index])
            print('Сохранено.')

        elif answer[0] == 'сортировать':
            if answer[1] == 'зп':
                if answer[2] == 'возрастание':
                    vacancies_list_objects.sort(key=lambda x: x._salary_from if x._salary_from is not None else 0, reverse=False)
                elif answer[2] == 'убывание':
                    vacancies_list_objects.sort(key=lambda x: x._salary_from if x._salary_from is not None else 0, reverse=True)
            for index, value in enumerate(vacancies_list_objects):
                print(f'{index}: {value}')

        elif answer[0] == 'назад':
            break
        elif answer[0] == 'выход':
            quit()
        elif answer[0] == 'получить' and answer[1] == 'помощь':
            get_help()
        else:
            print(answer, 'не является внутренней командой.')
