from collections import deque

chocolate = deque(int(x) for x in input().split(', '))
cups_milk = deque(int(x) for x in input().split(', '))
milkshakes = 0
while True:

    if milkshakes == 5 or len(chocolate) == 0 or len(cups_milk) == 0:
        break

    choco = chocolate.pop()
    milk = cups_milk.popleft()

    if choco == milk:
        milkshakes += 1
    else:
        if choco <= 0:
            cups_milk.appendleft(milk)
        elif milk <= 0:
            chocolate.append(choco)
        else:
            cups_milk.append(milk)
            choco -= 5
            chocolate.append(choco)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(*chocolate, sep=', ')
else:
    print("Chocolate: empty")

if cups_milk:
    print(*cups_milk, sep=', ')
else:
    print("Milk: empty")
