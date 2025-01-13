#Generate an identity matrix of size n x n.
n = int(input("Enter the size of the identity matrix: "))
for i in range(n):
    row = ['1' if i == j else '0' for j in range(n)]
    print(','.join(row))
