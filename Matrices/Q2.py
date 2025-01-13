#Multiply a square matrix A by a scalar s.
n = int(input("Enter the size of the matrix: "))
matrix = [list(map(int, input("Enter row: ").split())) for _ in range(n)]
s = int(input("Enter the scalar: "))
for row in matrix:
    print(' '.join(str(s * element) for element in row))