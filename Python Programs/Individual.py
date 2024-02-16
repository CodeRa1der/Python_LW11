#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add_route():
    # Запись данных маршрута
    first = input('Первая точка маршрута: ')
    second = input('Вторая точка маршрута: ')
    # Создание словаря
    return {
        'first': first,
        'second': second,
    }


def list_of_routes(roadway):
    if roadway:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 14,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^5} | {:^20} | {:^20} |'.format(
               "Номер маршрута",
                "Место отправки",
                "Место прибытия"
            )
        )
        print(line)
        # Вывод данных о маршрутах
        for number, route in enumerate(roadway, 1):
            print(
                '| {:<14} | {:<20} | {:<20} |'.format(
                    number,
                    route.get('first', ''),
                    route.get('second', '')
                )
            )
            print(line)
    else:
        print("Список маршрутов пуст")

def help():
    print('\nСписок команд:')
    print('help - Вывести этот список')
    print('add - Добавить маршрут')
    print('list - Показать список маршрутов')
    print('exit - Выйти из программы')

def main():
    # Список маршрутов
    routes = []
    # Начало бесконечного цикла команд
    while True:
        # Сюда вписывать команды
        command = input('>>> ').lower()

        # Команда help
        if command == 'help':
            help()

        # Команда add
        elif command == 'add':
            route = add_route()
            # Добавление словаря в список
            routes.append(route)

        # Команда list
        elif command == 'list':
            list_of_routes(routes)

        # Команда exit
        elif command == 'exit':
            break

        # Другая команда/неверно введенная команда
        else:
            print(f'Неизвестная команда {command}')

if __name__ == '__main__':
    main()
