# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        res = Complex(self.a + other.a, self.b + other.b)
        return res

    def __mul__(self, other):
        res = Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)
        return res

    def __str__(self):
        return f'{self.a}+{self.b}i'


a = Complex(2, 3)
b = Complex(1, -4)
d = Complex(4, 6)
e = Complex(8, -3)
c = b * a + a
f = d + e
print(f'({b})*({a})+({a}) = {c}')
print(f'({d})+({e}) = ({f})')
