from classes.json_processor.json_processor import JSONProcessor
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
        answer = input('Просмотр сохраненных вакансий: ').lower()
        if answer == 'назад':
            break
        elif answer.split()[0] == 'удалить':
            _index = int(answer.split()[1])
            json_proc.remove_from_favorites(_index)
            print('Удалено.')
        elif answer == 'выход':
            print('Досвидули.')
            quit()
        elif answer == 'получить помощь':
            get_help()
        else:
            print(answer, 'не является внутренней командой.')
    return


def _show_favorites():
    fav_list = JSONProcessor().show_favorites()
    if fav_list == 'error':
        print('Сохраненные вакансии не найдены. У вас нет сохраненных вакансий, либо файл сохранений поврежден.')
        return
    first_iterarion = True
    while True:
        for i in fav_list:
            if first_iterarion:
                print(i)
                first_iterarion = False
            answer = input('Просмотр сохраненных вакансий: ').lower()
            if answer == 'дальше':
                print(i)
            elif answer == 'назад':
                break
            elif answer == 'выход':
                quit()
            elif answer == 'получить помощь':
                get_help()
            else:
                print(answer, 'не является внутренней командой.')
        break
