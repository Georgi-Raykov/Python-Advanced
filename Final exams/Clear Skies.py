size = int(input())

matrix = []

j_row, j_col = 0, 0
jet_units = 300
enemy_count = 0
is_win = False
is_lose = False
for row in range(size):

    matrix.append(list(input()))
    for col in range(size):

        if matrix[row][col] == 'J':
            j_row, j_col = row, col
        elif matrix[row][col] == 'E':
            enemy_count += 1

positions = {'up': lambda r, c: (r - 1, c),
             'down': lambda r, c: (r + 1, c),
             'left': lambda r, c: (r, c - 1),
             'right': lambda r, c: (r, c + 1)}
while True:
    command = input()
    next_row, next_col = positions[command](j_row, j_col)

    matrix[j_row][j_col] = '-'

    if matrix[next_row][next_col] == 'E':
        j_row, j_col = next_row, next_col
        matrix[next_row][next_col] = 'J'
        jet_units -= 100
        if jet_units <= 0:
            is_lose = True
            break
        enemy_count -= 1
        if enemy_count == 0:
            is_win = True
            break
    elif matrix[next_row][next_col] == 'R':
        j_row, j_col = next_row, next_col
        matrix[next_row][next_col] = 'J'
        jet_units = 300
    else:
        j_row, j_col = next_row, next_col
        matrix[next_row][next_col] = 'J'


if is_win:
    print("Mission accomplished, you neutralized the aerial threat!")
elif is_lose:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{j_row}, {j_col}]")

for row in matrix:
    print(*row, sep='')