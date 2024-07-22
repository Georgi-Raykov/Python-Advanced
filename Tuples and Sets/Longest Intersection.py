n = int(input())
bigger_set = set()
for _ in range(n):

    first, second = input().split('-')

    start, end = [int(x) for x in first.split(',')]
    second_start, second_end = [int(x) for x in second.split(',')]

    first_set = set(range(start, end + 1))
    second_set = set(range(second_start, second_end + 1))

    result = first_set.intersection(second_set)
    if len(result) > len(bigger_set):
        bigger_set = result

print(f"Longest intersection is [{' '.join(str(x) for x in bigger_set)}] with length {len(bigger_set)}")
