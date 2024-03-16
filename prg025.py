def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

start_range = 10
end_range = 50
primes_in_range = find_primes_in_range(start_range, end_range)
print("Prime numbers in the range", start_range, "to", end_range, "are:", primes_in_range)