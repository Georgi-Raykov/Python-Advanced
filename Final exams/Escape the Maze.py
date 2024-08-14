size = int(input())

matrix = []
player_row, player_col = 0, 0
for row in range(size):

    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
player_health = 100
is_exit = False
is_dead = False
while True:

    command = input()

    next_row, next_col = directions[command](player_row, player_col)
    matrix[player_row][player_col] = '-'
    if 0 <= next_row < size and 0 <= next_col < size:

        if matrix[next_row][next_col] == 'X':
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'P'
            is_exit = True
            break

        if matrix[next_row][next_col] == 'M':
            player_health -= 40
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'P'
            if player_health <= 0:
                player_health = 0
                is_dead = True
                break

        elif matrix[next_row][next_col] == 'H':
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'P'
            if player_health + 15 > 100:
                player_health = 100
            else:
                player_health += 15
        else:
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'P'
if is_exit:
    print("Player escaped the maze. Danger passed!")
    print(f"Player's health: {player_health} units")
elif is_dead:
    print("Player is dead. Maze over!")
    print(f"Player's health: {player_health} units")
for row in matrix:
    print(*row, sep='')
