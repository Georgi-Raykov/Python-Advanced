first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):

    command = input().split()

    if command[0] == 'Add':

        if command[1] == 'First':

            first = first.union([int(x) for x in command[2:]])
        elif command[1] == 'Second':
            second = second.union([int(x) for x in command[2:]])

    elif command[0] == 'Remove':

        if command[1] == 'First':

            first = first.difference([int(x) for x in command[2:]])
        elif command[1] == 'Second':
            second = second.difference([int(x) for x in command[2:]])

    else:

        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
