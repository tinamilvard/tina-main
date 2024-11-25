# def vyprintuj_a_pust(func):
#     def nova_funkce(a,b):
#         print(f"pouštíme funkci {func.__name__} s parametry {a}, {b}")
#         return func(a,b)
#     return nova_funkce
#
# @vyprintuj_a_pust
# def soucet(a,b):
#     return a+b
#
# @vyprintuj_a_pust
# def rozdil(a,b):
#     return a-b
#
# print(soucet(3,5))
# print(rozdil(3,5))


def with_password(func):
    password = "tanicka"

    def nova_funkcia(a,b):

        if input("napis heslo: ") == password:
            print("heslo je spravne")
            return func(a,b)
        else:
            return"heslo je ne spravne"
    return nova_funkcia


@with_password
def soucet(a,b):
    return a+b

@with_password
def rozdil(a,b):
    return a-b

print(soucet(7,9))
print(rozdil(8,4))
