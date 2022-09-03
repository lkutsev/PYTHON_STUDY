# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re


class MyData:
    def __init__(self, mystr):
        self.str = mystr

    @classmethod
    def to_number(cls, str_dt):
        res = list(map(int, re.findall('\d+', str_dt)))
        res = cls.validate(res)
        return res

    @staticmethod
    def validate(res):
        rets = str(res)
        #      print (res[0])
        if (len(res) != 3):
            rets += ' _Неверный формат даты: должео быть три значения, дата месяц год'
        if (res[0] < 1) or (res[0] > 31):
            rets += f' _Неверный формат даты: День месяца ({res[0]}) от 1 до 31'
        if (res[1] < 1) or (res[1] > 12):
            rets += f'_Неверный формат даты: Месяц ({res[1]}) от 1 до 12'
        if (res[1] < 0) or (res[1] > 3000):
            rets += f'_Неверный формат даты: Год ({res[2]}) от 0 до 3000'
        return rets


print(MyData.to_number('12.12.2333'))
print(MyData.to_number('12.2333'))
print(MyData.to_number('90.12.2333'))
print(MyData.to_number('12.122.2333'))
