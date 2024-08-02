size = int(input())

matrix = []
alice_row, alice_col = 0, 0
for row in range(size):

    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            alice_row, alice_col = row, col

directions = {

    'up': lambda a, b: (a - 1, b),
    'down': lambda a, b: (a + 1, b),
    'right': lambda a, b: (a, b + 1),
    'left': lambda a, b: (a, b - 1)
}
tea = 0
is_fail = False
is_won = False
while True:

    command = input()

    row, col = directions[command](alice_row, alice_col)
    matrix[alice_row][alice_col] = '*'
    if row < 0 or row >= size or col < 0 or col >= size:
        is_fail = True
        break

    if matrix[row][col] == 'R':
        is_fail = True
        matrix[row][col] = '*'
        break

    elif matrix[row][col].isdigit():

        tea += int(matrix[row][col])
        alice_row, alice_col = row, col
        matrix[alice_row][alice_col] = '*'
    else:
        alice_row, alice_col = row, col
        matrix[alice_row][alice_col] = '*'

    if tea >= 10:
        is_won = True
        break

if is_fail:
    print("Alice didn't make it to the tea party.")
elif is_won:
    print("She did it! She went to the party.")
for row in matrix:
    print(*row, sep=' ')

