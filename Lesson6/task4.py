# #Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print(self.name, 'is now going')

    def stop(self):
        print(self.name, 'is now stopping')

    def turn(self, direction):
        print(self.name, 'is now turn on a ', direction)

    def showspeed(self):
        print('Speed = ', self.speed)

    def get_params(self):
        return (self.name + ' ' + self.color + ' police! ' if self.is_police else '')


class TownCar(Car):
    name = 'volvo'
    color = 'white'

    def showspeed(self):
        Car.showspeed(self)
        if self.speed > 60: print('превышение скорости 60 км!')


class SportCar(Car):
    name = 'Bugatti'
    color = 'red'


class WorkCar(Car):
    name = 'kamaz'
    color = 'green'

    def showspeed(self):
        Car.showspeed(self)
        if self.speed > 40: print('превышение скорости 40 км!')


class PoliceCar(Car):
    name = 'uaz'
    color = 'white'
    is_police = True


wc = WorkCar()
wc.showspeed()
wc.go()
wc.speed = 50
wc.showspeed()

pc = PoliceCar()
pc.showspeed()
pc.go()
pc.speed = 50
pc.showspeed()
print(pc.get_params())
