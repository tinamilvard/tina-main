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
#
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


class Bird:
    def walk(self):
        print("1")


class fish:
    def walk(self):
        print("2")


class Animal(Bird, fish):
    pass
animal = Animal()
animal.walk()