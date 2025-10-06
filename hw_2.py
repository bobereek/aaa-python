import csv


def make_hierarchy(data: list):
    """
    Функция для создания иерархии команд.
    Получает на вход список, каждый элемент которого - это список с данными.
    Функция группирует команды по департаментам и возвращает словарь, где ключи - это департаменты, а значения - это множества команд в департаменте.
    """
    hierarchy = {}
    for row in data:
        depart = row[1]
        part = row[2]
        if depart in hierarchy:
            hierarchy[depart].add(part)
        else:
            hierarchy[depart] = set()
            hierarchy[depart].add(part)
    return hierarchy


def print_hierarchy(data: list):
    """
    Функция для вывода иерархии команд.
    Получает на вход список, каждый элемент которого - это список с данными.
    Функция вызывает функцию для создания иерархии команд и выводит ее в консоль.
    """
    hierarchy = make_hierarchy(data)

    for depart in hierarchy:
        val = hierarchy[depart]
        print(f"""Департамент: {depart}
              \t Отделы: {", ".join(val)}""")


def make_report(data: list):
    """
    Функция для создания отчёта по департаментам.
    Получает на вход список, каждый элемент которого - это список с данными.
    Функция группирует команды по департаментам, вычисляет метрики и возвращает отчёт по департаментам.
    """
    report_data = {}
    for row in data:
        depart = row[1]
        if depart in report_data:
            report_data[depart]["count"] += 1
            report_data[depart]["min_salary"] = min(
                report_data[depart]["min_salary"], int(row[5])
            )
            report_data[depart]["max_salary"] = max(
                report_data[depart]["max_salary"], int(row[5])
            )
            report_data[depart]["total_salary"] += int(row[5])
        else:
            report_data[depart] = {
                "count": 1,
                "min_salary": float("inf"),
                "max_salary": 0,
                "total_salary": 0,
            }

    return report_data


def print_report(data: list):
    """
    Функция для вывода отчёта по департаментам.
    Получает на вход список, каждый элемент которого - это список с данными.
    Функция вызывает функцию для создания отчета по входным данным и выводит его в консоль.
    """
    report_data = make_report(data)

    for depart in report_data:
        print(
            f"""Департамент: {depart}
            \t Численность: {report_data[depart]["count"]}, Вилка: {report_data[depart]["min_salary"]} - {report_data[depart]["max_salary"]}, Средняя зарплата: {report_data[depart]["total_salary"] / report_data[depart]["count"]}"""
        )


def save_report(data: list):
    """
    Функция для сохранения отчёта по департаментам.
    Получает на вход список, каждый элемент которого - это список с данными.
    Функция получает путь для сохранения файла и вызывает функцию для создания отчета по входным данным, сохраняет созданный отчет в файл.
    """
    print("Введите путь для сохранения файла:")
    path = input()
    report_data = make_report(data)

    with open(path, mode="w", encoding="utf-8") as file:
        for depart in report_data:
            file.write(
                f"""Департамент: {depart}
                \t Численность: {report_data[depart]["count"]}, Вилка: {report_data[depart]["min_salary"]} - {report_data[depart]["max_salary"]}, Средняя зарплата: {round(report_data[depart]["total_salary"] / report_data[depart]["count"], 2)}\n"""
            )


def show_menu():
    """
    Функция для вывода меню.
    Выводит меню.
    """
    print()
    print("Введите команду")
    print("1. Вывести иерархию команд")
    print("2. Вывести сводный отчёт по департаментам")
    print("3. Сохранить сводный отчёт")
    print("0. Выход")


def menu(data: list):
    """
    Функция для вывода меню и обработки команд.
    Выводит меню команд, ждёт ввода и вызывает необходимую функцию.
    На вход получает список data, который после передает в функции для обработки.
    """
    show_menu()
    command = int(input())

    while command not in [0, 1, 2, 3]:
        command = int(input())
        print("Некорректный ввод, повторите попытку")
    while command != 0:
        if command == 1:
            print_hierarchy(data)
        elif command == 2:
            print_report(data)
        elif command == 3:
            save_report(data)
        show_menu()
        command = int(input())
    return


def start():
    """
    Функция для запуска программы.
    Она выводит запрос на ввод пути к csv-файлу, читает файл и передаёт его содержимое в функцию menu.
    После завершения работы функции menu выводит сообщение о завершении программы.
    """
    print("Введите путь к csv-файлу")

    path = input()
    with open(path, "r", newline="\n", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        data = list(reader)[1:]

    menu(data)
    print("Программа завершена")


if __name__ == "__main__":
    start()
