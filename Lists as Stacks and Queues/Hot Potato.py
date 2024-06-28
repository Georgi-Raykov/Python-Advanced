from collections import deque

kids = deque(input().split())
toss = int(input())

counter = 1
while len(kids) > 1:

    kid = kids.popleft()
    if counter == toss:
        counter = 1
        print(f"Removed {kid}")

    else:
        kids.append(kid)
        counter += 1



print(f"Last is {''.join(kids)}")
