from collections import deque

amount_money = deque(int(x) for x in input().split())
prices = deque(int(x) for x in input().split())
eaten_foods = 0
while amount_money and prices:

    money = amount_money.pop()
    price = prices.popleft()

    if money == price:
        eaten_foods += 1
    elif money > price:
        money -= price
        eaten_foods += 1
        if len(amount_money) > 0:
            amount_money[-1] += money
if eaten_foods >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_foods} foods.")
elif 2 <= eaten_foods < 4:
    print(f"Henry ate: {eaten_foods} foods.")
elif eaten_foods == 1:
    print(f"Henry ate: {eaten_foods} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
