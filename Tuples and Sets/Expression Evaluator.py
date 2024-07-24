from collections import deque

line = input().split()

line2 = deque()

operators = {'-': lambda a, b: a - b,
             '+': lambda a, b: a + b,
             '*': lambda a, b: a * b,
             '/': lambda a, b: a // b}

for x in line:

    if x in '+-*/':

        while len(line2) > 1:
            left = line2.popleft()
            right = line2.popleft()
            result = operators[x](left, right)
            line2.appendleft(result)
    else:
        line2.append(int(x))
print(*line2)