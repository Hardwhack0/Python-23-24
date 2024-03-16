def prevod_na_hodiny(dny, hodiny):
    celkove_hodiny = dny * 24 + hodiny
    return celkove_hodiny

dny = int(input("Zadej počet dnů: "))
hodiny = int(input("Zadej počet hodin: "))

vysledek = prevod_na_hodiny(dny, hodiny)
print(f"{dny} dní a {hodiny} hodin je celkem {vysledek} hodin.")