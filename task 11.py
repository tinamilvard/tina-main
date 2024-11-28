#Task 11 - udělat iterátor, kterému řekneme kolik chceme čísel, např. 5.
#Iterátor bude postupně vracet mocniny těchto čísel. Tzn pro číslo 5, iterátor vrátí 1, 4, 9, 16, 25
from Task7 import budova

# mocniny = IteratorMocnin(5)
# for mocnina in mocniny:
#     print(mocnina)

#1
#4
#9
#16
#25


class IteratorMocnin:
    def __init__(self, n):
        self.kolik = n
        self.cislo = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cislo > self.kolik:
            raise StopIteration
        result = self.cislo ** 2
        self.cislo += 1
        return result

mocniny = IteratorMocnin(5)
for mocnina in mocniny:
    print(mocnina)
mocniny = IteratorMocnin(6)
for mocnina in mocniny:
    print(mocnina)