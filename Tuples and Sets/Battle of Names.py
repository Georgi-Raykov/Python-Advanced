n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()

    current_result = sum([ord(x) for x in name]) // i

    if current_result % 2 == 0:
        even_set.add(current_result)
    else:
        odd_set.add(current_result)
if sum(odd_set) == sum(even_set):

    result = odd_set.union(even_set)
    print(*result, sep=', ')
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
    print(*result, sep=', ')
elif sum(odd_set) < sum(even_set):
    result = odd_set.symmetric_difference(even_set)
    print(*result, sep=', ')
