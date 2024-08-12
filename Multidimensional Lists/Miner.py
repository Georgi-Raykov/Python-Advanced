def get_position(pos, r, c, mtx):
    if pos == 'up':
        if 0 <= r - 1 < len(mtx):
            r = r - 1
    elif pos == 'right':
        if 0 <= c + 1 < len(mtx):
            c = c + 1
    elif pos == 'left':
        if 0 <= c - 1 < len(mtx):
            c = c - 1
    elif pos == 'down':
        if 0 <= r + 1 < len(mtx):
            r = r + 1
    return [r, c]


size = int(input())

commands = input().split()
matrix = []
coals = 0
collected_coals = 0
row_position, col_position = 0, 0

for row in range(size):
    matrix.append(input().split())

    for col in range(size):

        if matrix[row][col] == 's':
            row_position, col_position = row, col
        if matrix[row][col] == 'c':
            coals += 1
is_end = False
for direction in commands:
    position = get_position(direction, row_position, col_position, matrix)
    matrix[row_position][col_position] = '*'
    if matrix[position[0]][position[1]] == 'c':
        collected_coals += 1
        matrix[position[0]][position[1]] = '*'
    row_position, col_position = position[0], position[1]
    if matrix[position[0]][position[1]] == 'e':
        is_end = True
        break

if collected_coals == coals:
    print(f"You collected all coal! ({row_position}, {col_position})")
elif is_end:
    print(f"Game over! ({row_position}, {col_position})")
else:
    print(f"{coals - collected_coals} pieces of coal left. ({row_position}, {col_position})")
