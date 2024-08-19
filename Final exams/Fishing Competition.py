def if_in_matrix_size(r, c, size):
    return 0 <= r < size and 0 <= c < size


def if_out_bounders(r, c, size):
    if r >= size:
        r = 0
        return r, c
    elif r < 0:
        r = size - 1
        return r, c
    elif c >= size:
        c = 0
        return r, c
    elif c < 0:
        c = size - 1
        return r, c


size = int(input())

matrix = []

s_row, s_col = 0, 0
quota = 0
for row in range(size):
    matrix.append([str(x) for x in input()])
    for col in range(size):
        if matrix[row][col] == 'S':
            s_row, s_col = row, col

position = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)

}
is_whirlpool = False
while True:

    command = input()
    if command == 'collect the nets':
        break

    next_row, next_col = position[command](s_row, s_col)
    matrix[s_row][s_col] = '-'

    if not if_in_matrix_size(next_row, next_col, size):
        next_row, next_col = if_out_bounders(next_row, next_col, size)

    if matrix[next_row][next_col].isdigit():
        quota += int(matrix[next_row][next_col])
        s_row, s_col = next_row, next_col
        matrix[s_row][s_col] = 'S'
    elif matrix[next_row][next_col] == 'W':
        s_row, s_col = next_row, next_col
        matrix[s_row][s_col] = 'S'
        is_whirlpool = True
        break
    else:
        s_row, s_col = next_row, next_col
        matrix[s_row][s_col] = 'S'
if is_whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship:"
          f"[{s_row},{s_col}] ")
elif quota >= 20:
    print("Success! You managed to reach the quota!")
    print(f"Amount of fish caught: {quota} tons.")
    for row in matrix:
        print(*row, sep='')
elif quota < 20:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - quota} tons of fish more.")
    print(f"Amount of fish caught: {quota} tons.")
    for row in matrix:
        print(*row, sep='')


# example input
# 5
# S---9
# 777-1
# --5--
# 11W11
# 988--
# down
# down
# down
# down
# down
# down
# right
# right
# right
# collect the nets
