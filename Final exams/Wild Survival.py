from collections import deque

bees = deque(int(x) for x in input().split())
bee_eaters = deque(int(x) for x in input().split())

while bees and bee_eaters:

    bee = bees.popleft()
    bee_eater = bee_eaters.pop()

    while True:

        if bee == 0 and bee_eater == 0:
            break
        elif bee_eater <= 0:
            bees.append(bee)
            break
        elif bee < 7 or bee <= 0:
            bee_eaters.append(bee_eater)
            break

        else:
            bee -= 7
            bee_eater -= 1

print("The final battle is over!")

if not bees and not bee_eaters:
    print("But no one made it alive!")

if bees:
    print(f"Bee groups left: {', '.join(str(x) for x in bees)}")
if bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")
