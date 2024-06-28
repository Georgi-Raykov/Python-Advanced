from collections import deque

litters = int(input())

people = deque()

while True:

    name = input()

    if name == 'Start':
        break
    people.append(name)

while True:

    line = input().split()

    if line[0] == 'End':
        break
    if len(line) == 2:
        water = int(line[1])
        litters += water
    else:
        person = people.popleft()
        water = int(line[0])
        if litters >= water:
            litters -= water
            print(f"{person} got water")
        else:
            print(f"{person} must wait")


print(f"{litters} liters left.")