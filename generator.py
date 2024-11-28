#Task12 - Vytvoříte generátor, který bude postupně vracet
# Albert - máme koncovku "bert".
# před tu koncovku budou dávány předpony "Al", "Ro", "Hu", "Nor", "Gil"
#
# def GeneratorJmen(pred, konc):
#     #TODO zde implementovat
#     pass
#
# predpony = ["Al", "Ro", "Hu", "Nor", "Gil"] #TODO dát dle svého jména
# koncovka = "bert" #TODO dát dle svého jména
# for jmeno in GeneratorJmen(predpony, koncovka):
#     print(f"Tvé jméno je {jmeno}") # Albert, Robert, Hubert, Norbert, Gilbert

def GeneratorJmen(pred, konc):
    for p in pred:
        yield p + konc
predpony = ["Teti", "Mari", "Teri", "lili", "Di", "Y", "D"]
koncovka = "ana"
for jmeno in GeneratorJmen(predpony, koncovka):
    print(f"Tvé jméno je {jmeno}")