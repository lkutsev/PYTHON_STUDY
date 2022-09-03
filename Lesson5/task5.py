# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint

try:
    f = open("tsk5.txt", "w", encoding="utf-8")
    i = [str(randint(0, 9)) for x in range(0, randint(0, 1000))]
    p = ' '.join(i)
    print(p)
    f.write(p)
    f.close()
except Exception as er:
    print('Error while creating file:', er)
try:
    f2 = open("tsk5.txt", "r", encoding="utf-8")
    l = f2.readline().split(' ')
    print(len(l))
    f2.close()
except Exception as er:
    print('Error while counting:', er)
