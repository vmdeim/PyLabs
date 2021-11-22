# Задание 1: Создание класса
from pprint import pprint
class Hobbit:
    def __init__(self, name, age, height, weight, kill):
        self.name, self.age, self.height, self.weight, self.kill = name, age, height, weight, kill
        self.key = (name, age)
    def __repr__(self):
        return "Hobbit('%s','%s','%s','%s','%s')" % (self.name, self.age, self.height,self.weight,self.kill)

hob1 = Hobbit("Бильбо Бэггинс",190,143,51,0)
hob2 = Hobbit("Фродо Бэггинс",89,153,55,0)
hob3 = Hobbit("Перегрин Тук",78,123,49,0)
hob4 = Hobbit("Сэмуайз Гэмджи",75,133,53,0)
hob5 = Hobbit("Смеагол",500,113,25,0)

hobbiton = {
    hob1.key: hob1,
    hob2.key: hob2,
    hob3.key: hob3,
    hob4.key: hob4,
    hob5.key: hob5,
}

pprint(hobbiton )
pprint(hobbiton [hob3.key])
print(type(hobbiton))

# Задание 2: Поиск по полям словаря


print(hobbiton.items())


