def out_side(row, col, rows, columns):
    return row < 0 or col < 0 or row >= rows or col >= columns


rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(list(input().split()))

while True:

    line = input().split()
    if line[0] == 'END':
        break

    row = int(line[1])
    col = int(line[2])
    row1 = int(line[3])
    col1 = int(line[4])
    if line[0] != 'swap' or len(line) != 5:
        print('Invalid input!')
        continue

    if out_side(row, col, rows, columns) or out_side(row1, col1, rows, columns):
        print('Invalid input!')
        continue

    matrix[row][col], matrix[row1][col1] = matrix[row1][col1], matrix[row][col]

    for row in matrix:
        print(*row, sep=' ')
