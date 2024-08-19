from collections import deque

monsters = deque(int(x) for x in input().split(','))
strikers = deque(int(x) for x in input().split(','))
killed_monsters = 0
while monsters and strikers:

    monster = monsters.popleft()
    striker = strikers.pop()

    if striker >= monster:
        killed_monsters += 1
        striker -= monster
        if striker != 0:
            if len(strikers) > 0:
                strikers[-1] += striker
    elif striker < monster:
        monster -= striker
        monsters.append(monster)

if not len(monsters):
    print("All monsters have been killed! ")
elif not len(strikers):
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")

# example input
# 30,25,40,35
# 15,20,10,30

# example input 2
# 20,15,10
# 5,15,10,25
