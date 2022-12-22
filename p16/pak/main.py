import sys


from pak.find_human import find_human
from pak.get_human import get_human
from pak.display_human import display_human


def main():
    """
    Главная функция программы.
    """
    # Список работников.
    people = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            human = get_human()

            # Добавить словарь в список.
            people.append(human)
            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('phone', 0))

        elif command == 'list':
            # Отобразить всех работников.
            display_human(people)

        elif command == 'find':
            f = input('Введите фамилию: ')

            # Выбрать людей с заданной фамилией.
            selected = find_human(people, f)
            # Отобразить выбранных работников.
            display_human(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("find - найти человека по фамилии;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

