from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
left_water = 0
while True:

    if len(cups) == 0 or len(bottles) == 0:
        if bottles:
            print(f"Bottles: {' '.join(map(str, bottles))}")
            print(f"Wasted litters of water: {left_water}.")
        else:
            print(f"Cups: {' '.join(map(str, cups))}")
            print(f"Wasted litters of water: {left_water}.")
        break

    cup = cups.popleft()
    bottle = bottles.pop()

    if bottle > cup:

        left_water += bottle - cup
    elif bottle < cup:

        cup -= bottle
        cups.appendleft(cup)

