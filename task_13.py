#Task 13 - zároveň sčítáme a násobíme

#cílem bude paralerně počítat:
# součet čísel 1,2,3,4,...1000000
# násobení čísel 1, 2, 3,4, .... 100


#Vložit třídu ThreadWithReturnValue

# definovat funkce pro sčítání a násobení

# inicializovat třídu ThreadWithReturnValue pro každou úlohu

# pustit  .start()

# počkat na výsledek .join()

# vysledek_scitani =
# vysledek_nasobeni =

# vyprintovat výsledky





# import threading
# import time
#
#
# class ThreadWithReturnValue(threading.Thread):
#     def __init__(self, target, args=(), kwargs=None):
#         if kwargs is None:
#             kwargs = {}
#         self.target = target
#         self.args = args
#         self.kwargs = kwargs
#         super().__init__()
#
#     def run(self):
#         self.result = self.target(*self.args, **self.kwargs)
#
#     def join(self, timeout=None):
#         super().join(timeout)
#         return self.result
#
#
# def print_cube(num):
#     # A function that returns the third power of a number given as a parameter
#     time.sleep(5)
#     print(f"Cube: {num * num * num}")
#
#
# def print_square(num):
#     # A function that returns the square of the number given as a parameter
#     time.sleep(5)
#     return num * num
#
#
# if __name__ == "__main__":
#     # creating threads
#     t1 = ThreadWithReturnValue(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
#
#     # starting threads
#     t1.start()
#     t2.start()
#
#     # waiting until both threads have finished executing before executing further code
#     print(t1.join())
#     t2.join()
#
#     print("Done!")


import threading

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result

def scitame():
    return sum(range(1, 1000001))

def nasobime():
    nasobka = 1
    for i in range(1, 101):
        nasobka *= i
    return nasobka

if __name__ == "__main__":
    scitame_thread = ThreadWithReturnValue(target=scitame)
    nasobime_thread = ThreadWithReturnValue(target=nasobime)

    scitame_thread.start()
    nasobime_thread.start()

    vysledek_scitani = scitame_thread.join()
    vysledek_nasobeni = nasobime_thread.join()

    # Print the results
    print(f"Výsledek sčítání: {vysledek_scitani}")
    print(f"Výsledek násobení: {vysledek_nasobeni}")
