#Write a function to calculate the factorial of a positive integer.
def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
n = int(input("Enter a number: "))
print(factorial(n))