def check_bounders(r, c, row, col):
    return 0 <= r < row and 0 <= c < col


rows, cols = [int(x) for x in input().split()]

matrix = []
b_row, b_col = 0, 0
amount_p = 0
amount_moves = 0
touched_players = 0
for row in range(rows):
    matrix.append([str(x) for x in input().split()])
    for col in range(cols):
        if matrix[row][col] == 'B':
            b_row, b_col = row, col
        elif matrix[row][col] == 'P':
            amount_p += 1
positions = {'up': lambda r, c: (r - 1, c),
             'down': lambda r, c: (r + 1, c),
             'left': lambda r, c: (r, c - 1),
             'right': lambda r, c: (r, c + 1)}
while True:

    command = input()
    if command == 'Finish':
        break
    next_row, next_col = positions[command](b_row, b_col)

    if check_bounders(next_row, next_col, rows, cols) and matrix[next_row][next_col] != 'O':

        if matrix[next_row][next_col] == 'P':
            amount_p -= 1
            touched_players += 1
            amount_moves += 1
            matrix[b_row][b_col] = '-'
            b_row, b_col = next_row, next_col
            matrix[next_row][next_col] = 'B'
        else:
            amount_moves += 1
            matrix[b_row][b_col] = '-'
            b_row, b_col = next_row, next_col
            matrix[next_row][next_col] = 'B'
    if amount_p == 0:
        break
print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {amount_moves}")

# input 1

# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish

# input 2

# 4 4
# O B O -
# - P O P
# - - P -
# - - - -
# left
# right
# down
# right
# down
# right
# up
# right
# up
# down
# Finish
