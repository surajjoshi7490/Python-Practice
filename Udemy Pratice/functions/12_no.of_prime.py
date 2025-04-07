n = 100
primes = []

for i in range(2, n + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

print(primes)
print("Total primes:", len(primes))
