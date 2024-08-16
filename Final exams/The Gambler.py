def in_bounders(r, c, size):
    return 0 <= r < size and 0 <= c < size


size = int(input())

matrix = []
g_row, g_col = 0, 0
money = 100
for row in range(size):

    matrix.append(list(input()))
    for col in range(size):

        if matrix[row][col] == 'G':
            g_row, g_col = row, col
positions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
is_win = False
is_lose = False
while True:

    command = input()
    if command == "End":
        break

    next_row, next_col = positions[command](g_row, g_col)
    matrix[g_row][g_col] = '-'

    if not in_bounders(next_row, next_col, size):
        is_lose = True
        break
    if matrix[next_row][next_col] == 'J':
        money += 100000
        g_row, g_col = next_row, next_col
        matrix[g_row][g_col] = 'G'
        is_win = True
        break
    elif matrix[next_row][next_col] == 'W':
        money += 100
        g_row, g_col = next_row, next_col
        matrix[g_row][g_col] = 'G'
    elif matrix[next_row][next_col] == 'P':
        money -= 200
        g_row, g_col = next_row, next_col
        matrix[g_row][g_col] = 'G'
        if money <= 0:
            is_lose = True
            break
    else:
        g_row, g_col = next_row, next_col
        matrix[g_row][g_col] = 'G'
if is_win:
    print("You win the Jackpot!")
    print(f"End of game. Total amount: {money}$")
    for row in matrix:
        print(*row, sep='')
elif is_lose:
    print("Game over! You lost everything!")
else:
    print(f"End of game. Total amount: {money}$")
    for row in matrix:
        print(*row, sep='')
