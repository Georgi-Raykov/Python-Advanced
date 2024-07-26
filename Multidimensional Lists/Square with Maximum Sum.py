rows, columns = [int(x) for x in input().split(', ')]

matrix = []
sum = 0
r, c = 0, 0
r1, c1 = 0, 0
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(rows - 1):
    current_sum = 0
    for col in range(columns - 1):

        current_sum = (matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1])
        if current_sum > sum:
            sum = current_sum
            r, c = matrix[row][col], matrix[row][col + 1]
            r1, c1 = matrix[row + 1][col], matrix[row + 1][col + 1]
print(f"{r} {c}")
print(f"{r1} {c1}")
print(sum)