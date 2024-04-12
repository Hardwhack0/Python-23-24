import random

def hazi_kostkou(pocet_hodu):
    """Simuluje házení kostkou daný početkrát a vrací počet padnutých stran."""
    vysledky = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0} 
    for _ in range(pocet_hodu):
        hod = random.randint(1, 6)  # Náhodný hod kostkou
        vysledky[hod] += 1  # Zvýšíme počet padnutých stran o 1
    return vysledky

# Počet hodů kostkou
pocet_hodu = 1000

# Házení kostkou
vysledky_hodu = hazi_kostkou(pocet_hodu)

# Výpis výsledků
print("Počet padnutých stran kostky:")
for strana, pocet in vysledky_hodu.items():
    print(f"Strana {strana}: {pocet}x")