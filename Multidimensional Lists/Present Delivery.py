def get_present_positions(r, c, sze):
    possible_positions = [
        [r + 1, c],
        [r - 1, c],
        [r, c - 1],
        [r, c + 1]
    ]
    result = []
    for row, col in possible_positions:
        if 0 <= row < sze and 0 <= col < sze:
            result.append([row, col])
    return result

presents = int(input())

size = int(input())

matrix = []
nice_kids = 0
nice_kids_total = 0
dave_gifts = 0
santa_row, santa_col = 0, 0
for row in range(size):

    matrix.append(input().split())
    for col in range(size):

        if matrix[row][col] == 'S':
            santa_row, santa_col = row, col
        elif matrix[row][col] == 'V':
            nice_kids += 1
            nice_kids_total += 1

positions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
while True:

    direction = input()
    if direction == 'Christmas morning':
        break

    row, col = positions[direction](santa_row, santa_col)
    matrix[santa_row][santa_col] = '-'
    if 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == 'V':
            presents -= 1
            nice_kids -= 1
            santa_row, santa_col = row, col
            matrix[santa_row][santa_col] = 'S'
        elif matrix[row][col] == 'C':
            santa_row, santa_col = row, col
            matrix[santa_row][santa_col] = 'S'
            position = get_present_positions(santa_row, santa_col, size)

            for row, col in position:
                if matrix[row][col] == 'V':
                    nice_kids -= 1
                    presents -= 1
                    matrix[row][col] = '-'
                elif matrix[row][col] == 'X':
                    presents -= 1
                    matrix[row][col] = '-'
        else:
            santa_row, santa_col = row, col
            matrix[row][col] = 'S'
        if presents == 0:
            break
if presents == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if nice_kids > 0:
    print(f"No presents for {nice_kids} nice kid/s.")
if nice_kids == 0:
        print(f"Good job, Santa! {nice_kids_total} happy nice kid/s.")



