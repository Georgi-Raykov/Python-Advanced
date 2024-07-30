def get_explosion(r, c, mtx):
    actions = [[r - 1, c - 1],
               [r - 1, c],
               [r - 1, c + 1],
               [r + 1, c + 1],
               [r + 1, c],
               [r + 1, c - 1],
               [r, c - 1],
               [r, c + 1]]
    result = []
    for left, right in actions:

        if 0 <= left < len(mtx) and 0 <= right < len(mtx) and mtx[left][right] > 0:
            result.append([left, right])
    return result


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

coordinates = input().split()

for bomb in coordinates:

    data = bomb.split(',')

    row, col = int(data[0]), int(data[1])
    power = matrix[row][col]
    if power <= 0:
        continue
    matrix[row][col] = 0
    detonation = get_explosion(row, col, matrix)

    for hit_row, hit_col in detonation:
        matrix[hit_row][hit_col] -= power

live_cells = 0
live_cell_sum = 0

for row in matrix:

    for el in row:

        if el > 0:
            live_cells += 1
            live_cell_sum += el

print(f"Alive cells: {live_cells}")
print(f"Sum: {live_cell_sum}")

for row in matrix:

    print(*row, sep=' ')
