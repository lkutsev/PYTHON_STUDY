# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
lst = list(input('введите текст (он же список):'))
print(f'введен список {lst}')
for i in range(0, len(lst), 2):
    if i + 1 < len(lst):
        lst.insert(i, lst.pop(i + 1))
print(f'получен список {lst}')
