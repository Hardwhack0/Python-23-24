def remainder_division(dividend, divisor):
    return dividend - ((dividend // divisor) * divisor)

dividend = 20
divisor = 3

result = remainder_division(dividend, divisor)
print("Zbytek po dělení", dividend, "a", divisor, "je:", result)