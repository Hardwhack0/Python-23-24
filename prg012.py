n = [2, 3, 5, 7, 10, 13] 

primes = []
for num in n:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)

print("Prvočísla zadaná v proměnné n jsou:", primes)