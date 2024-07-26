rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
total = 0
for row in range(rows):
    total += matrix[row][row]
print(total)
