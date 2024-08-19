from collections import deque

fuels = deque(int(x) for x in input().split())
consumption = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())
altitude = 0
reached_altitudes = []
while fuels and consumption:

    fuel = fuels.pop()
    consum = consumption.popleft()
    needed_fuel = fuel_needed.popleft()

    result = abs(fuel - consum)

    if result >= needed_fuel:
        altitude += 1
        reached_altitudes.append(f"Altitude {altitude}")
        print(f"John has reached: Altitude {altitude}")
    elif result < needed_fuel:
        altitude += 1
        print(f"John did not reach: Altitude {altitude}")
        break

if len(fuels) and reached_altitudes:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
elif len(fuels) and not reached_altitudes:

    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")

# input
# 40 66 123 100
# 10 30 70 33
# 40 55 77 100

# example 2
# 199 190 100 100
# 20 40 30 50
# 50 60 70 80
