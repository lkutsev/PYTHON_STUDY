# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(a, b):
    try:
        res = a / b
        print("res = ", res)
    except ZeroDivisionError:
        print('деление на ноль!')
        return
    except Exception as err2:
        print(err2)
        res = 0
    return res


while 1 == 1:
    try:
        i = input('Введите два числа через пробел:').split(' ')
        if i[0].upper() == 'Q': break
        if len(i) != 2:
            print("введены неверные параметры или формат не соответствует!")
            continue
        div(int(i[0]), int(i[1]))
    except Exception as err:
        print(err)
