rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix_row = []
    for col in range(columns):
        first_letter = chr(97 + row)
        second_letter = chr(97 + row + col)
        palindrome = first_letter + second_letter + first_letter
        matrix_row.append(palindrome)
    matrix.append(matrix_row)

for row in matrix:
    print(' '.join(row))
