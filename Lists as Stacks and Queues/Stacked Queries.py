

n = int(input())

numbers = []

for _ in range(n):

    line = input().split()

    if line[0] == '1':
        number = int(line[1])
        numbers.append(number)
    elif line[0] == '2':
        if numbers:
            numbers.pop()
    elif line[0] == '3':
        if numbers:
            max_value = max(numbers)
            print(max_value)

    elif line[0] == '4':
        if numbers:

            min_value = min(numbers)
            print(min_value)


result = numbers[::-1]

print(', '.join(map(str, result)))