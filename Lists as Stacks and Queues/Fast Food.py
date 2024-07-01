from collections import deque

food_for_day = int(input())

orders = deque(int(x) for x in input().split())
max_order = max(orders)
while True:

    if len(orders) == 0:
        print(max_order)
        print("Orders complete")
        break
    order = orders.popleft()
    if food_for_day < order:
        orders.appendleft(order)
        print(max_order)
        print(f"Orders left: {' '.join(map(str, orders))}")
        break
    food_for_day -= order



