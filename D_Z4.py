numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(1, len(numbers)):
    in_prime = True
    divider = 0
    for j in range(1, len(numbers) + 1):
        if numbers[i] % j == 0:
            divider += 1
        if divider >= 3:
            in_prime = False
            break
        else:
            in_prime = True
    if in_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(primes)
print(not_primes)
