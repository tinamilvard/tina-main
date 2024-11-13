# from copy import deepcopy
#
#
# class Garage:
#     def __init__(self):
#         self.spaces = []
#
#     def add_car(self, car_name):
#         self.spaces.append(car_name)
#
#
# brno_garage = Garage()
# brno_garage.add_car("Volvo")
# brno_garage.add_car("Maserati")
# print(f"V garáži brno je: {brno_garage.spaces}")
# # praha_garage = deepcopy(brno_garage)
# praha_garage = brno_garage
# print(f"V praha_garage je: {praha_garage.spaces}")
# praha_garage.add_car("Trabant")
# print("Do prahy jsme přidali trabanta")
# print(f"V garáži brno je: {brno_garage.spaces} id: {id(brno_garage)}")
# print(f"V praha_garage je: {praha_garage.spaces} id: {id(praha_garage)}")

from copy import deepcopy
class Budova:
    def __init__(self):
        self.patra = []

    def pridej_patro(self, patro):
        self.patra.append(patro)

    def get_copy(self):
        return deepcopy(self)
budova = Budova()
budova.pridej_patro("Kanceláře")
budova.pridej_patro("Laboratoř")
print("Původní budova patra:", budova.patra)   # Očekává se: ["Kanceláře", "Laboratoř"]
kopie_budovy = budova.get_copy()
kopie_budovy.pridej_patro("Střešní zahrada")
print("Kopie budovy patra:", kopie_budovy.patra)  # Očekává se: ["Kanceláře", "Laboratoř", "Střešní zahrada"]

# #NA TENTO KOD NESAHAT
# #Vytvoř novou instanci Budovy a přidej pár pater
# budova = Budova()
# budova.pridej_patro("Kanceláře")
# budova.pridej_patro("Laboratoř")

# # Vytvoř kopii budovy pomocí metody get_copy
# kopie_budovy = budova.get_copy()
# kopie_budovy.pridej_patro("Střešní zahrada")

# # Očekávaný výsledek: Budova má 2 patra, kopie budovy má 3 patra
# print("Původní budova patra:", budova.patra)   # Očekává se: ["Kanceláře", "Laboratoř"]
# print("Kopie budovy patra:", kopie_budovy.patra)  # Očekává se: ["Kanceláře", "Laboratoř", "Střešní zahrada"]

# # Testuje, zda původní budova nebyla ovlivněna změnami v kopii
# assert budova.patra == ["Kanceláře", "Laboratoř"], "Chyba: Původní budova byla změněna."
# assert kopie_budovy.patra == ["Kanceláře", "Laboratoř", "Střešní zahrada"], "Chyba: Kopie budovy nebyla správně vytvořena."

# print("Gratuluji, test prošel: Třída Budova správně implementuje přidávání pater a metodu get_copy.")