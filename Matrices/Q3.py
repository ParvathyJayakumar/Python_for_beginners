#Compute the transpose of a matrix.
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
n = int(input("Enter the number of rows/columns in the matrix: "))
matrix = [list(map(int, input().split())) for _ in range(n)]
transposed = transpose(matrix)
for row in transposed:
    print(" ".join(map(str, row)))