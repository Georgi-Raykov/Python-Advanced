def if_in_bounder(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
commands = input().split(', ')
matrix = []
s_row, s_col = 0, 0
for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 's':
            s_row, s_col = row, col

positions = {'up': lambda r, c: (r - 1, c),
             'down': lambda r, c: (r + 1, c),
             'left': lambda r, c: (r, c - 1),
             'right': lambda r, c: (r, c + 1)}
hazelnuts = 0
is_win = False
is_lose = False
is_out_field = False
while True:

    for command in commands:
        next_row, next_col = positions[command](s_row, s_col)

        if not if_in_bounder(next_row, next_col, size):
            is_out_field = True
            break
        elif matrix[next_row][next_col] == 't':
            is_lose = True
            break
        elif hazelnuts == 3:
            is_win = True
            break
        elif matrix[next_row][next_col] == 'h':
            hazelnuts += 1
            matrix[s_row][s_col] = '*'
            s_row, s_col = next_row, next_col
            matrix[s_row][s_col] = 's'
        else:
            matrix[s_row][s_col] = '*'
            s_row, s_col = next_row, next_col
            matrix[s_row][s_col] = 's'

    if is_lose:
        break
    elif is_win:
        break
    elif is_out_field:
        break
if is_out_field:
    print("The squirrel is out of the field.")
if 0 < hazelnuts < 3:
    print("there are more hazelnuts to collect.")
elif is_lose:
    print("Unfortunately, the squirrel stepped on a trap...")

elif is_win:
    print("Good job! You have collected all hazelnuts!")
print(f"Hazelnuts collected: {hazelnuts}")

# input 1

# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*
# *****

# input 2
# 4
# down, down, right, right
# *s*h
# ***h
# ***t
# h***

# input 3
# 4
# down, down, right, right
# h***
# ***h
# *s*t
# **h*
