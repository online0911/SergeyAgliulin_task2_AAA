import csv


def load_data(filename):
    """
    Загружает данные из CSV-файла.

    Args:
        filename (str): Имя файла для загрузки

    Returns:
        list: Список с данными о сотрудниках
    """
    with open("C:/Users/Сергей/Desktop/SergeyAgliulin_task2_AAA/Corp_Summary.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        return list(reader)[1:]


def get_hierarchy(data):
    """
    Выводит иерархию команд - департамент и все команды, которые входят в него.

    Args:
        data (list): Данные о сотрудниках

    Returns:
        str: Отформатированная строка с иерархией департаментов и команд
    """
    hierarchy = {}
    for line in data:
        department = line[1]
        team = line[2]

        if department in hierarchy:
            hierarchy[department].add(team)
        else:
            hierarchy[department] = {team}

    result = []
    for department, teams in hierarchy.items():
        result.append(f"{department}: {', '.join(sorted(teams))}")

    return '\n'.join(result)


def get_department_stats(data):
    """
    Выводит сводный отчёт по департаментам.

    Args:
        data (list): Данные о сотрудниках

    Returns:
        dict: Словарь с статистикой по департаментам
    """
    salaries = {}
    for line in data:
        department = line[1]
        salary = int(line[-1])

        if department in salaries:
            salaries[department].append(salary)
        else:
            salaries[department] = [salary]

    dep_stats = {}
    for department, salary_list in salaries.items():
        count = len(salary_list)
        min_salary = min(salary_list)
        max_salary = max(salary_list)
        avg_salary = round(sum(salary_list) / count, 2)

        dep_stats[department] = [str(count), str(min_salary),
                                 str(max_salary), str(avg_salary)]

    return dep_stats


def save_stats_to_csv(stats, filename):
    """
    Сохраняет сводный отчёт по департаментам в виде CSV-файла.

    Args:
        stats (dict): Статистика по департаментам
        filename (str): Имя файла для сохранения
    """
    headers = ["Название департамента", "Кол-во сотрудников",
               "Минимальная зарплата", "Максимальная зарплата", "Средняя зарплата"]

    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)

        for department, stat_values in stats.items():
            row = [department] + stat_values
            writer.writerow(row)


def display_stats(stats):
    """
    Выводит статистику по департаментам в читаемом формате.

    Args:
        stats (dict): Статистика по департаментам
    """
    for department, stat_values in stats.items():
        print(f"""
Название департамента - {department}
Кол-во сотрудников - {stat_values[0]}
Минимальная зарплата - {stat_values[1]}
Максимальная зарплата - {stat_values[2]}
Средняя зарплата - {stat_values[3]}""")


def main():
    """
    Основная функция программы.
    """
    data = load_data(
        "C:/Users/Сергей/Desktop/SergeyAgliulin_task2_AAA/Corp_Summary.csv")

    while True:
        print("\nМеню:")
        print("1. Вывести иерархию команд")
        print("2. Вывести сводный отчёт по департаментам")
        print("3. Сохранить сводный отчёт в CSV-файл")
        print("4. Выход")

        try:
            choice = input("Введите пункт меню (1-4): ")

            if choice == "1":
                print("\nИерархия команд:")
                print(get_hierarchy(data))

            elif choice == "2":
                print("\nСводный отчёт по департаментам:")
                stats = get_department_stats(data)
                display_stats(stats)

            elif choice == "3":
                stats = get_department_stats(data)
                save_stats_to_csv(stats, "Corp_stats.csv")
                print("Отчет успешно сохранен в файл Corp_stats.csv")

            elif choice == "4":
                print("Выход из программы.")
                break

            else:
                print("Неправильный пункт меню. Пожалуйста, выберите от 1 до 4.")

        except ValueError:
            print("Ошибка: введите число от 1 до 4.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
