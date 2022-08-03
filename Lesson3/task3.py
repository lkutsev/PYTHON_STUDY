# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    nums = [a, b, c]
    return sum(nums) - min(nums)


while 1:
    try:
        i = input('Введите три числа через пробел:').split(' ')
        if i[0].upper() == 'Q': break
        if len(i) != 3:
            print("введены неверные параметры или формат не соответствует!")
            continue

        print(f'Сумма двух максимальых аргументов={my_func(int(i[0]), int(i[1]), int(i[2]))}')
    except Exception as err:
        print(err)
