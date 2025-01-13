#Print the sum of all integers in the range [1000, 2000] divisible by both a and b.
a = int(input("Enter the first divisor: "))
b = int(input("Enter the second divisor: "))
total = 0
for i in range(1000, 2001):
    if i % a == 0 and i % b == 0:
        total += i
print(total)