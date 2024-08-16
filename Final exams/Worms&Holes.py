from collections import deque

worms = deque(int(x) for x in input().split())
holes = deque(int(x) for x in input().split())
matches = 0
while worms and holes:

    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
    else:

        worm -= 3
        if worm > 0:
            worms.append(worm)


if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")
if not worms and not holes:
    print("Every worm found a suitable hole!")
elif holes and not worms:
    print("Worms left: None")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: None")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")