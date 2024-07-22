n = int(input())
result = set()
for _ in range(n):

    line = set(input().split())

    result = result.union(line)

for el in result:
    print(el)