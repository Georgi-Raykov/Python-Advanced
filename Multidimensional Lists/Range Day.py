def get_next_position(r, c, d, v):
    if d == 'up':
        return r - v, c
    if d == 'down':
        return r + v, c
    if d == 'left':
        return r, c - v
    if d == 'right':
        return r, c + v


matrix = []

my_row, my_col = 0, 0
targets = 0
hit_targets = 0
track_targets = []
for row in range(5):

    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            my_row, my_col = row, col
        elif matrix[row][col] == 'x':
            targets += 1
            hit_targets += 1
positions = {

    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
n = int(input())
for _ in range(n):

    commands = input().split()

    if commands[0] == 'move':
        direction = commands[1]
        value = int(commands[2])
        row, col = get_next_position(my_row, my_col, direction, value)
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            my_row, my_col = row, col
    elif commands[0] == 'shoot':
        direction = commands[1]
        row, col = positions[direction](my_row, my_col)

        while 0 <= row < len(matrix) and 0 <= col < len(matrix):

            if matrix[row][col] == 'x':
                hit_targets -= 1
                track_targets.append([row, col])
                break
            row, col = positions[direction](row, col)

if hit_targets == 0:
    print(f"Training completed! All {targets} targets hit.")
    print(*track_targets, sep='\n')
else:
    print(f"Training not completed! {hit_targets} targets left")
    if track_targets:
        print(*track_targets, sep='\n')
