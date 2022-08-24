# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class odezda(ABC):
    @abstractmethod
    def rashod(self):
        pass


class palto(odezda):
    __v = 0

    def __init__(self, v):
        self.__v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v > 20 and v < 70:
            self.__v = v
        else:
            self.__v = self.__v
            print("Ошибка. Размер пальто может быть от 20ти до 70ти. Попытка присвоить ", v)

    def rashod(self):
        return self.__v / 6.5 + 0.5

    def __str__(self):
        return (f'Пальто, размер = {self.__v}, расход ткани = {self.rashod()}')


class kostum(odezda):
    def __init__(self, h):
        self.__h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h > 20 and h < 70:
            self.__h = h
        else:
            self.__h = self.__h
            print("Ошибка. Размер костюма может быть от 20ти до 70ти. Попытка присвоить ", h)

    def rashod(self):
        return self.__h * 2 + 0.3

    def __str__(self):
        return (f'Костюм, размер = {self.__h}, расход ткани = {self.rashod()}')


k1 = kostum(50)
p1 = palto(60)
p1.v = 110
p1.v = -10
print(p1)
print(k1)

odezda = [kostum(60), kostum(90), palto(70), palto(80)]
x = 0
for i in (odezda):
    print(i)
    x += i.rashod()
print("Общий расход = ", x)
