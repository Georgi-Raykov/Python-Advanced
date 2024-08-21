def in_bounders(r, c, row, col):
    return 0 <= r < row and 0 <= c < col


rows, cols = [int(x) for x in input().split(',')]

matrix = []

m_row, m_col = 0, 0

cheese_counter = 0

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'M':
            m_row, m_col = row, col
        elif matrix[row][col] == 'C':
            cheese_counter += 1
positions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

is_danger = False
while True:
    command = input()
    next_row, next_col = positions[command](m_row, m_col)

    if in_bounders(next_row, next_col, rows, cols):

        if matrix[next_row][next_col] == 'C':
            cheese_counter -= 1
            matrix[m_row][m_col] = '*'
            m_row, m_col = next_row, next_col
            matrix[m_row][m_col] = 'M'
            if cheese_counter == 0:
                print("Happy mouse! All the cheese is eaten , good night!")
                break
        elif matrix[next_row][next_col] == 'T':
            matrix[m_row][m_col] = '*'
            m_row, m_col = next_row, next_col
            matrix[m_row][m_col] = 'M'
            print("Mouse is trapped!")
            break
        elif command == 'danger':
            is_danger = True
            break
        elif matrix[next_row][next_col] == '*':
            matrix[m_row][m_col] = '*'
            m_row, m_col = next_row, next_col
            matrix[m_row][m_col] = 'M'
    else:

        print("No more cheese for tonight!")
        break
if is_danger and cheese_counter > 0:
    print("Mouse will come later!")

for row in matrix:
    print(*row, sep='')

# input

# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left
# down
# down
# down
# right
# danger

# input 2

# 4,8
# CC@**C*M
# T*@**CT*
# **@@@@**
# T***C***
# down
# right
# left
# down
# left
# danger

# input 3

# 6,3
# @CC
# @TC
# @C*
# @M*
# @**
# @**
# left
# up
# left
# right
# up
# up
# left
# left
# danger
