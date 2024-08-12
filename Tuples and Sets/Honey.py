from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
operator = deque(input().split())

operators = {'-': lambda a, b: a - b,
             '+': lambda a, b: a + b,
             '*': lambda a, b: a * b,
             '/': lambda a, b: a // b}
total = 0
while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    act = operator.popleft()

    if bee > nectar:
        bees.appendleft(bee)
        operator.appendleft(act)
    elif bee <= nectar:

        total += abs(operators[act](bee, nectar))

print(f"Total honey made: {total}")

if bees:
    print(*bees, sep=', ')
if nectars:
    print(*nectars, sep=', ')
