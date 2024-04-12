def calculate_sum(input_list):
    total = 0
    for number in input_list:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]
total_sum = calculate_sum(numbers)
print(total_sum) 