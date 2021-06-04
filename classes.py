# Создаём чертёж собаки
class Dog:
    def __init__(self):
        print('Я родился')

    def bark(self):
        print('Муда-муда')

    def tail_wag(self):
        print('*Виляю хвостом*')


# Создаём чертёж кота
class Cat:
    def __init__(self):
        print('Я родился')

    def meow(self):
        print('Мяу')

    def tail_wag(self):
        print('*Виляю хвостом*')


# Создаём объект собаки
# dio = Dog()
# bobik = Dog()
# cat = Cat()
# cat.introduce_yourself('Itachi', 7, "mangeku sharingan")
# cat.meow()
# dio.bark()


class Ninja:
    def __init__(self, name, age, sharingan):
        self.name = name
        self.age = age
        self.sharingan = sharingan

    def smoke_bombs(self):
        print('*Бросил дымовые бомбы*')

    def shadow_clone(self):
        print('Теневое клонирование!')

    def eat_ramen(self):
        print('Itadakimasu!')

    def introduce_yourself(self):
        print(f'Меня зовут {self.name}. Мне {self.age} лет и у меня {self.sharingan}')

    def print_name(self):
        print(self.name)


ninja = Ninja('Kakachi', 32, "mangeku sharingan")
# ninja.shadow_clone()
# ninja.eat_ramen()
ninja.introduce_yourself()
# self и объект ninja - одно и то же. Это объект ниндзи.
# print(ninja)
# ninja.print_name()
# print(ninja.name)


# По чертежу Ninja создать реальный объект ниндзи и заставить его кинуть дымовые бомбы
# *Прописать ниндзе ещё 2 способности и заставить его их применить
