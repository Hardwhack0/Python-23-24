def spocitej_prumer(cisla):
    pocet_cisel = len(cisla)
    soucet = sum(cisla)
    prumer = soucet / pocet_cisel
    return prumer

cisla = []

while True:
    cislo = input("Zadej číslo (pro ukončení zadej 'konec'): ")
    if cislo.lower() == 'konec':
        break
    cisla.append(float(cislo))

if cisla:
    prumer = spocitej_prumer(cisla)
    print("Průměr zadaných čísel je:", prumer)
else:
    print("Nezadali jste žádná čísla.")