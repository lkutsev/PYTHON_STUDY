# #Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод c (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep
import turtle


class TrafficLight:
    __color = ''

    def running(self):
        self.__color = 'red'
        self.__draw(7)
        self.__color = 'yellow'
        self.__draw(2)
        self.__color = 'green'
        self.__draw(1)

    def __draw(self, time):
        svetofor = turtle.Turtle()
        svetofor.color('black', self.__color)
        svetofor.begin_fill()
        svetofor.circle(100)
        svetofor.end_fill()
        sleep(time)


a = TrafficLight()
a.running()
