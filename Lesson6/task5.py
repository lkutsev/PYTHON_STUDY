# #vРеализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Pen. Title = ', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Pencil. Title = ', self.title)


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Handle. Title = ', self.title)


a = [Pen, Pencil, Handle]
for i in a:
    b = i()
    b.title = b.__class__
    b.draw()
