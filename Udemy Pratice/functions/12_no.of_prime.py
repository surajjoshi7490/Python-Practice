def count_primes(n):
    primes = []  # List to store prime numbers
    
    for i in range(2, n + 1):  # Loop through numbers 2 to n
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # Check divisors up to the square root of i
            if i % j == 0:  # If divisible, it's not prime
                is_prime = False
                break  # Exit the loop early if not prime
        if is_prime:  # If still marked as prime, add it to the list
            primes.append(i)
    
    return primes  # Return the list of primes

print(count_primes(100))