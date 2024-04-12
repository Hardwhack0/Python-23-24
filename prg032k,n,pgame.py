import random

def hra_kamen_nuzky_papir(volba_hrace):
    """Simuluje hru Kámen, nůžky, papír proti počítači."""
    moznosti = ['kámen', 'nůžky', 'papír']
    volba_pocitace = random.choice(moznosti)
    
    print(f"Tvoje volba: {volba_hrace}")
    print(f"Volba počítače: {volba_pocitace}")

    if volba_hrace == volba_pocitace:
        return "Remíza!"
    elif (volba_hrace == 'kámen' and volba_pocitace == 'nůžky') or \
         (volba_hrace == 'nůžky' and volba_pocitace == 'papír') or \
         (volba_hrace == 'papír' and volba_pocitace == 'kámen'):
        return "Vyhrál jsi!"
    else:
        return "Počítač vyhrál!"

print("Vítejte ve hře Kámen, nůžky, papír!")

while True:
    volba_hrace = input("Zvolte kámen, nůžky nebo papír (pro ukončení zadejte 'konec'): ").lower()
    
    if volba_hrace in ['kámen', 'nůžky', 'papír']:
        vysledek = hra_kamen_nuzky_papir(volba_hrace)
        print(vysledek)
    elif volba_hrace == 'konec':
        print("Konec hry. Děkujeme za hraní!")
        break
    else:
        print("Neplatná volba! Zadejte prosím 'kámen', 'nůžky', 'papír' nebo 'konec'.")