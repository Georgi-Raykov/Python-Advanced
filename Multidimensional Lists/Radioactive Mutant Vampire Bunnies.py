def get_new_position(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'D':
        return row + 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1


def outside(row, col, r, c):
    return row < 0 or row >= r and col < 0 or col >= c


def get_children(row, col, rs, cs):
    possible_children = [[row + 1, col],
                         [row - 1, col],
                         [row, col + 1],
                         [row, col - 1]]
    result = []
    for children_row, children_col in possible_children:
        if not outside(children_row, children_col, rs, cs):
            result.append([children_row, children_col])
    return result


rows, cols = [int(x) for x in input().split()]

matrix = []

player_row, player_col = 0, 0
bunnies = set()
for row in range(rows):
    matrix.append(list(input()))

    for col in range(cols):

        if matrix[row][col] == 'P':
            player_row, player_col = row, col
        elif matrix[row][col] == 'B':
            bunnies.add(f"{row} {col}")

command = input()

win = False
dead = False
for direction in command:

    new_row, new_col = get_new_position(player_row, player_col, direction)
    matrix[player_row][player_col] = '.'
    if outside(new_row, new_col, rows, cols):
        win = True

    elif matrix[new_row][new_col] == 'B':
        dead = True
        player_row, player_col = new_row, new_col
    else:

        matrix[new_row][new_col] = 'P'
        player_row, player_col = new_row, new_col
    new_bunnies = set()
    for bunny in bunnies:
        child_row, child_col = [int(x) for x in bunny.split()]

        children = get_children(child_row, child_col, rows, cols)
        for new_b_row, new_b_col in children:
            new_bunnies.add(f"{new_b_col} {new_b_col}")
            matrix[new_b_row][new_b_col] = 'B'
            if new_b_row == player_row and new_b_col == player_col:
                dead = True
    bunnies = bunnies.union(new_bunnies)

    if win or dead:
        break

for row in matrix:
    print(''.join(row))

if win:

    print(f"won: {player_row} {player_col}")
elif dead:
    print(f"dead: {player_row} {player_col}")