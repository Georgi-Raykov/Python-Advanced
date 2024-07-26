rows = int(input())

matrix = []

for _ in range(rows):

    matrix.append(list(input()))

symbol = input()
is_found = False
r, c = 0, 0
for row in range(rows):

    for col in range(rows):

        if matrix[row][col] == symbol:
            is_found = True
            r, c = row, col
            break
    if is_found:
        break

if is_found:
    print(f"({r}, {c})")
else:
    print(f"{symbol} does not occur in the matrix")
