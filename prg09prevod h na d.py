def prevod_na_dny_hodiny(hodiny):
    dny = hodiny // 24
    zbyle_hodiny = hodiny % 24
    return dny, zbyle_hodiny

hodiny = int(input("Zadej počet hodin: "))

dny, zbyle_hodiny = prevod_na_dny_hodiny(hodiny)
print(f"{hodiny} hodin je celkem {dny} dní a {zbyle_hodiny} hodin.")