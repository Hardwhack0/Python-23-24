start = int(input("Zadejte základní číslo: "))
end = int(input("Zadejte koncový číslo: "))

for i in range(start, end + 1):
    if i != end:
        print(i, end=", ")
    else:
        print(i)