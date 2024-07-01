clothes = [int(x) for x in input().split()]

rack_capacity = int(input())
current_rack = rack_capacity
counter = 1

while True:

    if len(clothes) == 0:
        break

    last_dress = clothes[-1]

    if current_rack - last_dress >= 0:
        dress = clothes.pop()

        current_rack -= dress
    else:
        counter += 1
        current_rack = rack_capacity
print(counter)