def find_hourse(row, col, size, mtx):
    possible_moves = [[row - 2, col - 1],
                      [row - 2, col + 1],
                      [row - 1, col - 2],
                      [row - 1, col + 2],
                      [row + 1, col - 2],
                      [row + 1, col + 2],
                      [row + 2, col - 1],
                      [row + 2, col + 1]]
    counter = 0
    for hourse_row, hourse_col in possible_moves:
        if 0 <= hourse_row < size and 0 <= hourse_col < size and mtx[hourse_row][hourse_col] == 'K':
            counter += 1

    return counter


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))
removed_horses = 0
while True:
    K_row, K_col = 0, 0
    best_count = 0
    best_row, best_col = 0, 0

    for row in range(size):

        for col in range(size):

            if matrix[row][col] == 'K':
                K_row, K_col = row, col
                count = find_hourse(K_row, K_col, size, matrix)
                if count > best_count:
                    best_count = count
                    best_row, best_col = K_row, K_col
    if best_count == 0:
        break
    else:
        matrix[best_row][best_col] = '0'
        removed_horses += 1

print(removed_horses)