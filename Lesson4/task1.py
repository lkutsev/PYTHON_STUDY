# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

_, hours, stavka, bonus = argv
try:
    result = (int(hours) * int(stavka)) + int(bonus)
    print(result)
except Exception as err:
    print('ошибка: ', err)
