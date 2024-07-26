rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    total = 0
    for row in range(rows):
        total += matrix[row][col]
    print(total)
