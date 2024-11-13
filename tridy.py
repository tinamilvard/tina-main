# from idlelib.colorizer import color_config
#
#
# class Car:
#
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         self.mileage = 0
#     def go_shopping(self):
#         self.mileage =+ 10
#     def go_for_gas(self):
#         self.mileage = + 23
#     def __str__(self):
#         return f"Brand: {self.brand} color: {self.color} with {self.mileage}km"
#
# class ElectricCar(Car):
#     pass
#     self.mileage += 8
#
#     car1 = Car( brand:"Ferrari", color "Red")
#     print(car1.brand)
#     print(car1)
#     car1.go_shopping()
#     print(car1)

# class Car:
#     def __init__(self, brand, color, mileage=0):
#         self.brand = brand
#         self.color = color
#         self.mileage = mileage
#
#     def go_shopping(self):
#         self.mileage += 10
#
#     def go_for_gas(self):
#         self.mileage += 23
#
#     def __str__(self):
#         return f"Brand: {self.brand} color: {self.color} with {self.mileage}km"
#
# class ElectricCar(Car):
#     def go_shopping(self):
#         super().go_shopping()
#         self.mileage += 8
#
# car1 = ElectricCar("Ferrari", "Red")
# car2 = ElectricCar("Skoda", "SuperB", 340000)
#
# print(car1.brand)
# print(car1)
#
# car1.go_shopping()
# car1.go_shopping()
# car1.go_shopping()
#
# print(car1)
# print(car2)


# class Animal:
#     total_weight = 0
#     def __init__(self, weight, age):
#         self.weight = weight
#         self.age = age
#
#     def look(self):
#         return "Look"
#
#     def breathe(self):
#         return "Breat"
#
#     @classmethod
#     def set_weight(cls):
#         cls.total_weight += 10


# class Fish(Animal):
#     def swim(self):
#         return "Swim"
#
#
# class Bird(Animal):
#     def fly(self):
#         return "Fly"
#
#
# class Mammal(Animal):
#     def run(self):
#         return "Running"
#
#
#
# class DomesticDog(Mammal):
#     def __init__(self, weight, age, breed, coat_color):
#         super().__init__(weight, age)
#         self.breed = breed
#         self.coat_color = coat_color
#
#     def bark(self):
#         return "Bark"
#
#     def retrieve(self):
#         return "Retrieve"
#
#
#
# animal = Animal(5, 5)
# print(animal.look())
# print(animal.breathe())
#
# fish = Fish(1, 1)
# print(fish.swim())
#
# bird = Bird(2,2 )
# print(bird.fly())
#
# mammal = Mammal(4, 4)
# print(mammal.run())
#
# dog = DomesticDog(6, 6, "Labrador", "Brown")
# print(dog.bark())
# print(dog.retrieve())
# print(dog.run())

# #task 5
# class Bird:
#     def walk(self):
#         print("1")
#
#
# class fish:
#     def walk(self):
#         print("2")
#
#
# class Animal(Bird, fish):
#     pass
# animal = Animal()
# animal.walk()

# class Obec:
#     pocet_obci = 0
#     def __init__(self, pocet_obyvatel):
#         self.pocet_obyvatel = pocet_obyvatel
#         Obec.pocet_obci += 1
#
#     @classmethod
#     def pridej_obec(cls):
#         cls.pocet_obci += 2
#
# praha = Obec(1000000) #praha.pocet_obyvatel - v nějakym místě uchováno
# brno = Obec(500000)  #brno.pocet_obyvatel - v jinym místě uchováno
# ostrava = Obec(310000)
# praha.pocet_obyvatel = 1100000
# ostrava.pridej_obec()
# Obec.pridej_obec()
# print(f"Počet obcí: {praha.pocet_obci}")
# print(f"Počet obcí: {brno.pocet_obci}")
# print(f"Počet obcí: {Obec.pocet_obci}")

#task 6.1
# class Animal:
#     total_weight = 0
#
#     def __init__(self, weight, age):
#         self.weight = weight
#         self.age = age
#         Animal.add_weight(weight)
#
#     def look(self):
#         return "Look"
#
#     def breathe(self):
#         return "Breat"
#
#     @classmethod
#     def add_weight(cls, weight):
#         cls.total_weight += weight
#
#     @classmethod
#     def subtract_weight(cls, weight):
#         cls.total_weight -= weight
#
#     def set_weight(self, new_weight):
#         # Adjust total weight by subtracting the old weight and adding the new weight
#         Animal.subtract_weight(self.weight)
#         self.weight = new_weight
#         Animal.add_weight(new_weight)
#
# class Fish(Animal):
#     def swim(self):
#         return "Swim"
#
# class Bird(Animal):
#     def fly(self):
#         return "Fly"
#
# class Mammal(Animal):
#     def run(self):
#         return "Running"
#
# class DomesticDog(Mammal):
#     def __init__(self, weight, age, breed, coat_color):
#         super().__init__(weight, age)
#         self.breed = breed
#         self.coat_color = coat_color
#
#     def bark(self):
#         return "Bark"
#
#     def retrieve(self):
#         return "Retrieve"
#
#
# animal1 = Fish(5, 5)
# animal2 = Bird(2, 3)
# print(f"Total weight: {animal1.total_weight}")
#
#
# animal1.set_weight(6)
# animal2.set_weight(3)
# print(f"Update: {animal1.total_weight}")

class Animal:
    total_weight = 0

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
        Animal.add_weight(weight)

    def look(self):
        return "Look"

    def breathe(self):
        return "Breathe"

    @classmethod
    def add_weight(cls, weight):
        cls.total_weight += weight

    @classmethod
    def subtract_weight(cls, weight):
        cls.total_weight -= weight

    def set_weight(self, new_weight):
        Animal.subtract_weight(self.weight)
        self.weight = new_weight
        Animal.add_weight(new_weight)

class Fish(Animal):
    def swim(self):
        return "Swim"

class Bird(Animal):
    def fly(self):
        return "Fly"

class Mammal(Animal):
    def run(self):
        return "Running"

class DomesticDog(Mammal):
    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        return "Bark"

    def retrieve(self):
        return "Retrieve"


animal1 = Fish(5, 5)
animal2 = Bird(2, 3)
animal3 = DomesticDog(10, 4, "bulldogek", "blue")


animals = [animal1, animal2, animal3]


for animal in animals:
    print(f"Weight: {animal.weight}")


