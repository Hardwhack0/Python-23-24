def calculate_factorial(number):
    result = 1
    current_number = 1
    while current_number <= number:
        result *= current_number
        current_number += 1
    return result

input_number = 5
factorial_result = calculate_factorial(input_number)
print(factorial_result) 