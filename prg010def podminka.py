def over_podminku(x, y):
    if 4*x + 3 < 5*y - 1:
        return True
    else:
        return False

x = float(input("Zadej hodnotu x: "))
y = float(input("Zadej hodnotu y: "))

if over_podminku(x, y):
    print("Podmínka 4x + 3 < 5y - 1 je splněná.")
else:
    print("Podmínka 4x + 3 < 5y - 1 není splněná.")