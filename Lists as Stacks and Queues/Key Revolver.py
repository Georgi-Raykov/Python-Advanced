from collections import deque

price_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence = int(input())
barrel_capacity_counter = 0
shoot_counter = 0
while True:

    if barrel_capacity_counter == size_of_gun_barrel and len(bullets) > 0:
        barrel_capacity_counter = 0
        print("Reloading!")

    if len(bullets) == 0 or len(locks) == 0:

        if len(locks) > 0:
            print(f"Couldn't get through. Locks left: {len(locks)}")
        else:
            bullets_cost = shoot_counter * price_bullet
            earned = intelligence - bullets_cost
            print(f"{len(bullets)} bullets left. Earned {earned}$")

        break
    shoot_counter += 1

    barrel_capacity_counter += 1

    bullet = bullets.pop()
    lock = locks.popleft()
    if bullet > lock:
        locks.appendleft(lock)
        print("Ping!")
    else:
        print('Bang!')
