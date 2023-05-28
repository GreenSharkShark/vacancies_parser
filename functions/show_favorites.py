from classes.json_processor import JSONProcessor
from functions.get_help import get_help


def show_favorites():
    json_proc = JSONProcessor()
    fav_list = json_proc.show_favorites()
    if fav_list == 'error':
        print('Сохраненные вакансии не найдены. У вас нет сохраненных вакансий, либо файл сохранений поврежден.')
        return
    for index, value in enumerate(fav_list):
        print(f'{index}: {value}')

    while True:
        answer = input('Просмотр сохраненных вакансий: ').lower().split()
        if answer[0] == 'назад':
            break

        elif answer[0] == 'сортировать':
            if answer[1] == 'зп':
                if answer[2] == 'возрастание':
                    fav_list.sort(key=lambda x: x._salary_from if x._salary_from is not None else 0, reverse=False)
                elif answer[2] == 'убывание':
                    fav_list.sort(key=lambda x: x._salary_from if x._salary_from is not None else 0, reverse=True)
            for index, value in enumerate(fav_list):
                print(f'{index}: {value}')

        elif answer[0] == 'удалить':
            try:
                _index = int(answer[1])
            except ValueError:
                print('Неправильны номер удаляемой вакансии.')
                continue
            json_proc.remove_from_favorites(_index)
            print('Удалено.')
        elif answer[0] == 'выход':
            print('Досвидули.')
            quit()
        elif answer[0] == 'получить помощь':
            get_help()
        else:
            print(answer, 'не является внутренней командой.')
    return
