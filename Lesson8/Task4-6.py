# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.
from abc import ABC, abstractmethod


class WarehouseOverFlow(Exception):
    def __str__(self):
        return ('На складе нет места!')


class SerialDuplicate(Exception):
    def __str__(self):
        return ('Серийный номер уже есть на складе!')


class PriceError(Exception):
    def __str__(self):
        return ('Указана недопустимая цена за товар')


class BrandError(Exception):
    def __str__(self):
        return ('Указан недопустимый бренд')


class WeigthError(Exception):
    def __str__(self):
        return ('Указан недопустимый вес')


class Store(ABC):
    stock = []
    name = ''

    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name

    @abstractmethod
    def addToStock(self, item):
        self.stock.append(item)

    @abstractmethod
    def delFromStock(self, item):
        try:
            self.stock.remove(item)
            return True
        except Exception as err:
            return False

    def __str__(self):
        r = ''
        for x in self.stock:
            r += str(x) + '\n'
        return str(r)


class Warehouse(Store):
    address = ''
    name = ''

    def checkSerial(self, item):
        try:
            if item.serial in (x.serial for x in self.stock):
                return True
            else:
                return False
        except Exception as err:
            print(err)
            return False

    def addToStock(self, item):
        try:
            if self.capacity <= len(self.stock):
                raise WarehouseOverFlow
            if self.checkSerial(item):
                raise SerialDuplicate
            self.stock.append(item)
        except WarehouseOverFlow as werr:
            print(f'Ошибка приемки на склад:{self.name}:{werr}')
        except SerialDuplicate as serr:
            print(f'Ошибка приемки {item} на склад {self.name}: {serr}')

    def delFromStock(self, item):
        Store.delFromStock(Store, item)


class OfficeEquipment(ABC):
    price = 0
    weigth = 0
    brand = ''
    serial = 0
    type = ''

    @abstractmethod
    def __init__(self, price, brand, weigth, serial):
        pass

    def __str__(self):
        return f'type = {self.type},\t brand = {self.brand},\t price = {self.price},\t weigth = {self.weigth},\t serial = {self.serial}'

    @abstractmethod
    def checkAtrributes(self, price, brand, weight):
        try:
            err = 'Зафиксированы ошибки при добавлении устройства '
            if price < 10 or price > 1000000:
                raise PriceError
            if brand not in ('CANON', 'HP', 'SAMSUNG'):
                raise BrandError
            if weight < 0.1 and weight > 1000:
                raise WeigthError
            return True
        except PriceError:
            print(f'Не могу добавить {self.type}: {PriceError} цена должна быть от 10 до 1000000')
            return False
        except Exception:
            print(Exception)
            return False


class Printer(OfficeEquipment):
    isColor = False
    speed = 0
    type = 'Printer'

    def __init__(self, price, brand, weigth, serial, isColor=False, speed=0):
        self.price = price
        self.brand = brand
        self.speed = speed
        self.weigth = weigth
        self.isColor = isColor
        self.serial = serial

    def checkAtrributes(self, price, brand, weight, speed):
        if OfficeEquipment.checkAtrributes(price, brand, weight):
            if speed > 1000 or speed < 1:
                print('Принтер не может печатать медленнее 1 и более 10000 страниц в минуту')
                return False
            return True


class Scanner(OfficeEquipment):
    isColor = False
    speed = 0
    type = 'Scanner'

    def __init__(self, price, brand, weigth, serial, isColor=False, speed=0):
        self.price = price
        self.brand = brand
        self.speed = speed
        self.weigth = weigth
        self.isColor = isColor
        self.serial = serial

    def checkAtrributes(self, price, brand, weight, speed):
        if OfficeEquipment.checkAtrributes(price, brand, weight):
            if speed > 100 or speed < 1:
                print('Сканер не может Сканировать медленнее 1 и более 1000 страниц в минуту')
                return False
            return True


class Xerox(OfficeEquipment):
    isColor = False
    type = 'Xerox'

    def __init__(self, price, brand, weigth, serial, isColor=False):
        self.price = price
        self.brand = brand
        self.weigth = weigth
        self.serial = serial

    def checkAtrributes(self, price, brand, weight):
        return OfficeEquipment.checkAtrributes(price, brand, weight)


wh1 = Warehouse(5, 'Moscow WH')
p1 = Printer(100, 'Canon', 3, '010101')
p2 = Printer(102, 'Canon', 2, '010102', True)
p3 = Printer(10, 'AXXX', 1, '3475734657')
s1 = Scanner(100, 'Canon', 3, '010104')

print(p1)
print(wh1)
wh1.addToStock(p1)
wh1.addToStock(p2)
wh1.addToStock(p3)
wh1.addToStock(s1)
wh1.addToStock(s1)
print(wh1)
wh1.delFromStock(s1)
print(wh1)
