from collections import deque

pomps = int(input())

stations = deque()
for _ in range(pomps):
    stations.append([int(x) for x in input().split()])


for i in range(pomps):
    tank = 0
    is_failed = False

    for fuel, distance in stations:
        tank = tank + fuel - distance
        if tank < 0:
            is_failed = True
            break

    if is_failed:
        stations.append(stations.popleft())
    else:
        print(i)
        break
