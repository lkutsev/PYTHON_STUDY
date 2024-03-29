#  Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#  Каждый кортеж хранит информацию об отдельном товаре.
#  В кортеже должно быть два элемента — номер товара и словарь с параметрами,
#  то есть характеристиками товара: название, цена, количество, единица измерения.
#  Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
#
# [
# (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
# (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
# (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
#
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором
# каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
#
# {
# 'название': ['компьютер', 'принтер', 'сканер'],
# 'цена': [20000, 6000, 2000],
# 'количество': [5, 2, 7],
# 'ед': ['шт.']
# }
prods = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
for i in range(0, len(prods)):
    for j in prods[i][1]:
        prods[i][1][j] = input('Введите ' + j + ':')
print('Список введенных товаров:' + prods)
res = {}
for i in prods:
    print(i)
    for j, val in i[1].items():
        if j not in res:
            res[j] = []
        res[j].append(val)
        print(j + val)
print('аналитика о товарах:' + str(res))
