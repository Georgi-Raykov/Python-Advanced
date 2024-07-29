rows = int(input())

matrix = []

primary_diagonals = []
secondary_diagonals = []
for _ in range(rows):

    matrix.append(input().split(', '))

for row in range(rows):

    primary_diagonals.append(matrix[row][row])
    secondary_diagonals.append(matrix[row][rows - 1 - row])

print(f"Primary diagonal: {', '.join(primary_diagonals)}. Sum: {sum([int(x) for x in primary_diagonals])}")
print(f"Secondary diagonal: {', '.join(secondary_diagonals)}. Sum: {sum([int(x) for x in secondary_diagonals])}")