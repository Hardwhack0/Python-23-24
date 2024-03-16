import random

def generuj_rating():
    return random.randint(1000, 2500)

def generuj_hrace():
    jmeno = "Hráč " + str(random.randint(1, 100))
    rating = generuj_rating()
    return {"jmeno": jmeno, "rating": rating}

def simuluj_hrace():
    hrac = generuj_hrace()
    print("Jméno:", hrac["jmeno"])
    print("Rating:", hrac["rating"])
    vitezstvi = random.randint(0, 100)
    remize = random.randint(0, 100 - vitezstvi)
    prohry = 100 - vitezstvi - remize
    print("Vítězství:", vitezstvi)
    print("Remízy:", remize)
    print("Prohry:", prohry)
    return hrac

simuluj_hrace()