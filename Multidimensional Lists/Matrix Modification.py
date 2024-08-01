size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:

    line = input()
    if line == 'END':
        break
    command = line.split()
    row, col, value = [int(x) for x in command[1:]]

    if row < 0 or row >= size or col < 0 or col >= size:
        print('Invalid coordinates')
        continue
    if command[0] == 'Add':

        matrix[row][col] += value
    elif command[0] == 'Subtract':
        matrix[row][col] -= value

for row in matrix:

    print(*row, sep=' ')


