def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print("Vyberte operaci:")
print("1. Sčítání")
print("2. Násobení")

choice = input("Zadejte volbu (1/2): ")

num1 = float(input("Zadejte první číslo: "))
num2 = float(input("Zadejte druhé číslo: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "*", num2, "=", multiply(num1, num2))
else:
    print("Neplatná volba")