# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
print('enter strings for file:\n')
f = open("text_task1.txt", "w", encoding="utf-8")
st = '\n'
while st != '':
    st = input()
    f.write(st + '\n')
f.close()
