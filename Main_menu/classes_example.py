class Car:
    car_type = 'Машина'
    def __init__(self, name: str, color: str, year: int):
        self.name = name
        self.color = color
        self.year = year

    def __str__(self):
        return f'Автомобиль {self.name}, цвета {self.color} и {self.yesr} года выпуска'

    def hoin(self):
        print(f'Би би би делает {self.name}')

a = Car('Mazda', 'black', 2003)
b = Car('Toyota', 'green', 2010)
# print(a.name)
# print(a.color)
# print(a.year)
# print(b.name)
# print(b.color)
# print(b.year)

# a.hoin()
# b.hoin()

# print(a)
# print(b)
#
# a.spoiler = 'Big and Black'
# print(a.spoiler)
# print(b.spoiler)
