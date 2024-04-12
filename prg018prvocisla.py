def get_prime_numbers(input_list):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    prime_numbers = [x for x in input_list if is_prime(x)]
    return prime_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = get_prime_numbers(numbers)
print(prime_numbers) 