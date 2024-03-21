import random

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2
    
    return binary_num

random_decimal_number = random.randint(1, 100)
print(f"Náhodné číslo v desítkové soustavě: {random_decimal_number}")

binary_number = decimal_to_binary(random_decimal_number)
print(f"Binární číslo: {random_decimal_number}: {binary_number}")