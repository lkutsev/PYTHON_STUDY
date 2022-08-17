# #Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    name = 'NN'
    surname = 'SS'
    position = 'AA'
    _income = {"wage": 10, "bonus": 10}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(Worker._income['wage'] + self._income['bonus'])


a = Position()
a.get_full_name()
a.get_total_income()
b = Position()
b.surname = 'ddd'
b.name = 'sdfsdf'
b._income['wage'] = 100
b.get_full_name()
b.get_total_income()
