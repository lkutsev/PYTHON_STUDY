# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
ws = int(input('целое положительное число:'))
cnt = 1
max = 0
while (ws > 0):
    if max < ws % 10:
        max = ws % 10
    ws = ws // 10
print("res:%d"%max)
