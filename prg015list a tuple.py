def get_even_numbers(input_list):
    return [x for x in input_list if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)

def get_even_numbers_from_tuple(input_tuple):
    return tuple(x for x in input_tuple if x % 2 == 0)

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers_tuple = get_even_numbers_from_tuple(numbers_tuple)
print(even_numbers_tuple)