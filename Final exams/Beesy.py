def if_in_bound(r, c, size):
    return 0 <= r < size and 0 <= c < size


def check_if_is_outside(r, c, size):
    if r >= size:
        r = 0
    elif r < 0:
        r = size - 1
    if c >= size:
        c = 0
    elif c < 0:
        c = size - 1
    return r, c


size = int(input())
matrix = []

bee_row, bee_col = 0, 0
hive_row, hive_col = 0, 0
for row in range(size):

    matrix.append([str(x) for x in input()])

    for col in range(size):

        if matrix[row][col] == 'B':
            bee_row, bee_col = row, col
        elif matrix[row][col] == 'H':
            hive_row, hive_col = row, col

positions = {'up': lambda r, c: (r - 1, c),
             'down': lambda r, c: (r + 1, c),
             'left': lambda r, c: (r, c - 1),
             'right': lambda r, c: (r, c + 1)}

nectar = 0

bee_units = 15
regeneration_times = 0
is_hive = False

while True:
    command = input()

    next_row, next_col = positions[command](bee_row, bee_col)

    if not if_in_bound(next_row, next_col, size):
        next_row, next_col = check_if_is_outside(next_row, next_col, size)

    if matrix[next_row][next_col] == 'H':
        matrix[bee_row][bee_col] = '-'
        bee_row, bee_col = next_row, next_col
        matrix[next_row][next_col] = 'B'
        bee_units -= 1
        is_hive = True
        break

    matrix[bee_row][bee_col] = '-'

    if matrix[next_row][next_col].isdigit():
        nectar += int(matrix[next_row][next_col])
        bee_row, bee_col = next_row, next_col
        matrix[next_row][next_col] = 'B'
        bee_units -= 1
    else:
        bee_row, bee_col = next_row, next_col
        matrix[next_row][next_col] = 'B'
        bee_units -= 1
    if bee_units == 0 and nectar < 30:
        break
    elif bee_units == 0 and nectar >= 30:

        regeneration_times += 1
        if regeneration_times > 1:
            break
        else:
            bee_units = nectar - 30
            nectar = 30
            if bee_units == 0:
                break

if is_hive and nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {bee_units}")

elif is_hive and nectar < 30:
    print("Beesy did not managed to collect enough nectar.")
elif not is_hive and bee_units == 0:

    print("This is the end! Beesy ran out of energy.")

for row in matrix:
    print(*row, sep='')
