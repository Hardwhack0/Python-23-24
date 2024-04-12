import random
import string

def generuj_heslo(delka):
    znaky = string.ascii_letters + string.digits + string.punctuation
    heslo = ''.join(random.choice(znaky) for _ in range(delka))
    return heslo

pocet_hesel = int(input("Zadej počet hesel k vygenerování: "))
delka_hesla = int(input("Zadej délku hesla: "))

print("Vygenerovaná hesla:")
for _ in range(pocet_hesel):
    heslo = generuj_heslo(delka_hesla)
    print(heslo)