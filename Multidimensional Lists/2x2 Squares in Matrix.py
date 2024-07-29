rows, columns = [int(x) for x in input().split()]

matrix = []

finds = 0

for _ in range(rows):

    matrix.append(list(input().split()))


for row in range(rows - 1):

    for col in range(columns - 1):

        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:

            finds += 1

print(finds)