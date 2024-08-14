def is_in_bounders(r, c, sze):
    return 0 <= r < sze and 0 <= c < sze


size = int(input())

matrix = []
p_row, p_col = 0, 0
stars = 2
for row in range(size):

    matrix.append([x for x in input().split()])

    for col in range(size):
        if matrix[row][col] == 'P':
            p_row, p_col = row, col
positions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
while True:
    command = input()
    next_row, next_col = positions[command](p_row, p_col)
    if stars >= 10:
        break
    if not is_in_bounders(next_row, next_col, size):
        matrix[p_row][p_col] = '.'
        next_row, next_col = 0, 0
        p_row, p_col = next_row, next_col
        matrix[p_row][p_col] = 'P'

    if matrix[next_row][next_col] == '*':
        matrix[p_row][p_col] = '.'
        p_row, p_col = next_row, next_col
        matrix[p_row][p_col] = 'P'
        stars += 1
    elif matrix[next_row][next_col] == '#':
        stars -= 1
    else:
        matrix[p_row][p_col] = '.'
        p_row, p_col = next_row, next_col
        matrix[p_row][p_col] = 'P'

    if stars == 0:
        break
if stars >= 10:
    print("You won! You have collected 10 stars.")
    print(f"Your final position is: [{p_row}, {p_col}]")
elif stars == 0:
    print("Game over! You are out if any stars.")
    print(f"Your final position is: [{p_row}, {p_col}]")

for row in matrix:
    print(*row, sep=' ')