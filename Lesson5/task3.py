# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их
# окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести
# фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
f = open("text_task1.txt", "r", encoding="utf-8")
cnt = 0
sum = 0
try:
    print('Получают меньше 20к р:')
    for i in f:
        l = i.split(' ')
        if float(l[1]) < 20000:
            print(l[0])
        sum += float(l[1])
        cnt += 1
except Exception as err:
    print('ошибка:', err)
print(f'Сумма средней величины дохода сотрудников: {sum / cnt:.2f}')
