s = int(input('Введите одноразрядное десятичное положительное число:'))
res = s + 10*s + 100*s + 10*s+ s+ s
print("Вариант 1: %d"%res)
ss = str(s)
res2 = int(ss) + int(ss+ss) + int(ss+ss+ss)
print("Вариант 2: %d"%res2)
res3 = 123*s
print("Вариант 3: %d"%res3)