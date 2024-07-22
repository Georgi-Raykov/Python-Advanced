n, m = [int(x) for x in input().split()]

first = set()
second = set()

for _ in range(n):

    name = input()
    first.add(name)

for _ in range(m):

    name = input()
    second.add(name)

result = first.intersection(second)


print(*result, sep='\n')