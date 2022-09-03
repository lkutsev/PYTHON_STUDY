# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyException(Exception):
    def __str__(self):
        return ('Я сам поймал деление на ноль!')


a = int(input('enter a:'))
b = int(input('enter b:'))

try:
    if b == 0:
        raise MyException
    print(a / b)
except MyException as err1:
    print(err1)
except Exception as err:
    print(err)
