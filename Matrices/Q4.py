#Check if a matrix is a magic square.
def is_magic_square(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])
    for i in range(n):
        if sum(matrix[i]) != target_sum or sum(row[i] for row in matrix) != target_sum:
            return False
    if sum(matrix[i][i] for i in range(n)) != target_sum or sum(matrix[i][n - i - 1] for i in range(n)) != target_sum:
        return False
    return True
n = int(input("Enter the size of the square matrix: "))
matrix = [list(map(int, input("Enter row: ").split())) for _ in range(n)]
print("YES" if is_magic_square(matrix) else "NO")
