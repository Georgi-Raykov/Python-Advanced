def in_boundaries(r, c, row, col):
    return 0 <= r < row and 0 <= c < col


rows, cols = [int(x) for x in input().split()]

matrix = []
b_row, b_col = 0, 0
starting_row, starting_col = 0, 0
for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):

        if matrix[row][col] == 'B':
            b_row, b_col = row, col
            starting_row, starting_col = row, col

positions = {'up': lambda r, c: (r - 1, c),
             'down': lambda r, c: (r + 1, c),
             'left': lambda r, c: (r, c - 1),
             'right': lambda r, c: (r, c + 1)}
while True:

    command = input()

    next_row, next_col = positions[command](b_row, b_col)

    if not in_boundaries(next_row, next_col, rows, cols):
        print("The delivery is late. Order is canceled.")
        matrix[starting_row][starting_col] = ' '
        break
    elif matrix[next_row][next_col] == 'P':
        matrix[b_row][b_col] = '.'
        b_row, b_col = next_row, next_col
        matrix[b_row][b_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
    elif matrix[next_row][next_col] == 'A':
        print("Pizza is delivered on time! Next order...")
        matrix[b_row][b_col] = '.'
        b_row, b_col = next_row, next_col
        matrix[b_row][b_col] = 'P'
        matrix[starting_row][starting_col] = 'B'
        break
    elif matrix[next_row][next_col] == '-':
        if matrix[b_row][b_col] != 'R':
            matrix[b_row][b_col] = '.'
        b_row, b_col = next_row, next_col
        matrix[next_row][next_col] = 'B'

for row in matrix:
    print(*row, sep='')

# example input

# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# right
# right
# right
# right
# up
# up
# up

# example input 2

# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# left
# right
# right
# right
# right
# right
# up
