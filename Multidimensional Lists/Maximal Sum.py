rows, columns = [int(x) for x in input().split()]

matrix = []

sum_numbers = float('-inf')
a, b, c, d, e, f, g, k, l = 0, 0, 0, 0, 0, 0, 0, 0, 0
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):

    for col in range(columns - 2):

        result = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] \
                 + matrix[row + 1][col] + matrix[row + 1][col + 1] \
                 + matrix[row + 1][col + 2] + matrix[row + 2][col] \
                 + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if result > sum_numbers:
            sum_numbers = result
            a, b, c, d, e, f, g, k, l = matrix[row][col], matrix[row][col + 1], matrix[row][col + 2], \
                                        matrix[row + 1][col], matrix[row + 1][col + 1], \
                                        matrix[row + 1][col + 2], matrix[row + 2][col], \
                                        matrix[row + 2][col + 1], matrix[row + 2][col + 2]

print(f"Sum: {sum_numbers}")
print(f"{a} {b} {c}")
print(f"{d} {e} {f}")
print(f"{g} {k} {l}")
