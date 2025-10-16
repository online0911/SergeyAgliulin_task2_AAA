with open("Corp_Summary.csv", 'r', encoding='utf-8') as dset:
  initial_data = list(map(lambda x: x.split(';'), dset.read().splitlines()))[1:]

def option_1():
  '''
  Выводит иерархию команд - департамент и все команды, которые входят в него.
    
  Returns:
    Отформатированная строка с иерархией департаментов и команд
  '''  
  hierarchy = {}
  for line in initial_data:
    if line[1] in hierarchy.keys():
      hierarchy[line[1]].add(line[3])
    else:
      hierarchy[line[1]] = {line[3]}
  return '\n'.join([f'{dep}: {", ".join(stats)}' for dep, stats in hierarchy.items()])


def option_2():
  '''
  Выводит сводный отчёт по департаментам: название, численность, вилка зарплат, средняя зарплата.
    
  Returns:
    Словарь с статистикой по департаментам
  '''
  salaries = {}
  for line in initial_data:
    if line[1] in salaries.keys():
      salaries[line[1]].append(int(line[-1]))
    else:
      salaries[line[1]] = [int(line[-1])]
  dep_stats = {}
  for dep, sal in salaries.items():
    dep_stats[dep] = list(map(str, [len(sal), min(sal), max(sal), round(sum(sal)/len(sal), 2)]))
  return dep_stats


def option_3():
  '''
    Сохраняет сводный отчёт по департаментам в виде CSV-файла.
  '''
  result_str = ''
  dep_stats = option_2()
  for dep in dep_stats:
    result_str += f"\n{dep};{';'.join(dep_stats[dep])}"
  with open('Corp_stats.csv', 'w', encoding='utf-8') as result:
    result.write('Название департамента;Кол-во сотрудников;Минимальная зарплата;Максимальная зарплата;Средняя зарплата')
    result.write(result_str)


if __name__ == '__main__':
  choice = int(input('Введите пункт меню (1-3): '))
  while True:
    if choice == 1:
      print(option_1())
      break
    elif choice == 2:
      for dep, stats in option_2().items():
        print(f'''
      
      Название департамента - {dep}
      Кол-во сотрудников - {stats[0]}
      Минимальная зарплата - {stats[1]}
      Максимальная зарплата - {stats[2]}
      Средняя зарплата - {stats[3]}''')
      break
    elif choice == 3:
      option_3()
      print('Отчет создан!')
      break
    else:
      print('Вы выбрали неправильный пункт меню.')