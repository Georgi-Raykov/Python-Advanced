rows = int(input())

matrix = []

for _ in range(rows):

    matrix.append(int(x) for x in input().split(', '))

flattened = [element for row in matrix for element in row]

print(flattened)