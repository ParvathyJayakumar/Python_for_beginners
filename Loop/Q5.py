#Find all solutions to the equation x^2 + y^2 = z^2 where x, y, z are positive integers and x < y < z < n.
n = int(input("Enter the limit: "))
found_solution = False
for x in range(1, n):
    for y in range(x + 1, n):
        for z in range(y + 1, n):
            if x**2 + y**2 == z**2:
                print(f"{x},{y},{z}")
                found_solution = True
if not found_solution:
    print("NO SOLUTION")
