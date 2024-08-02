size = int(input())

matrix = []


bunny_row, bunny_col = 0, 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny_row, bunny_col = row, col
moves = {
    'left': lambda a, b: (a, b - 1),
    'up': lambda a, b: (a - 1, b),
    'right': lambda a, b: (a, b + 1),
    'down': lambda a, b: (a + 1, b)
}

best_sum = float('-inf')
best_path = []
best_direction = ''
for direction in moves:

    current_sum = 0
    current_path = []
    row, col = moves[direction](bunny_row, bunny_col)

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
        current_sum += int(matrix[row][col])
        current_path.append([row, col])
        row, col = moves[direction](row, col)

    if current_sum > best_sum:
        best_sum = current_sum
        best_path = current_path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(best_sum)
