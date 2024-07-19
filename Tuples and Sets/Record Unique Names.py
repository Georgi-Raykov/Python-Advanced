n = int(input())
unique = set()
for _ in range(n):

    name = input()

    unique.add(name)

for name in unique:

    print(name)