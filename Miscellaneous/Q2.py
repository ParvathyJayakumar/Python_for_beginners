#Write a Python function to calculate the Manhattan distance of a robot based on its movements (UP, DOWN, LEFT, RIGHT).
def manhattan_distance(movements):
    x, y = 0, 0
    for move in movements:
        if move == "UP":
            y += 1
        elif move == "DOWN":
            y -= 1
        elif move == "LEFT":
            x -= 1
        elif move == "RIGHT":
            x += 1
    return abs(x) + abs(y)

movements = []
while True:
    move = input("Enter movement (or STOP to end): ")
    if move == "STOP":
        break
    movements.append(move)

print(manhattan_distance(movements))
