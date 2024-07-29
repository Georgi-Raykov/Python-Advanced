rows = int(input())

matrix = []

primary_diagonals = []
secondary_diagonals = []
for _ in range(rows):

    matrix.append(input().split())

for row in range(rows):

    primary_diagonals.append(matrix[row][row])
    secondary_diagonals.append(matrix[row][rows - 1 - row])

first = sum([int(x) for x in primary_diagonals])
second = sum([int(x) for x in secondary_diagonals])

result = first - second

print(abs(result))