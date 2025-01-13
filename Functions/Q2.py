#Write a function to find all prime factors of a given number n.
def prime_factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            is_prime = all(i % j != 0 for j in range(2, int(i**0.5) + 1))
            if is_prime:
                print(i)
n = int(input("Enter a number: "))
prime_factors(n)