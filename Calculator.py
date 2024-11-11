prve_cislo = int(input("vloz prve cislo: "))
znamienko = input("vloz znak pozadovane matematicke operace (+, -, *, /): ")
druhe_cislo = int(input("vloz druhe cislo: "))

if znamienko == "+":
    print(f"soucet cisel {prve_cislo} a {druhe_cislo} je {prve_cislo + druhe_cislo}")
elif znamienko == "-":
    print(f"rozdil cisel {prve_cislo} a {druhe_cislo} je {prve_cislo - druhe_cislo}")
elif znamienko == "*":
    print(f"soucin cisel {prve_cislo} a {druhe_cislo} je {prve_cislo * druhe_cislo}")
elif znamienko == "/":
    try:

    print(f"podil cisel {prve_cislo} a {druhe_cislo} je {prve_cislo / druhe_cislo}")
else:
    print(f"zvolil jsi chybnou operaci, program bude ukoncen")