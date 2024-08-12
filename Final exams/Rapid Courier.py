from collections import deque

packages = deque(int(x) for x in input().split())
couriers = deque(int(x) for x in input().split())

total_weight = 0

while packages and couriers:

    package = packages.pop()
    courier = couriers.popleft()

    if courier >= package:
        courier -= package * 2

        if courier > 0:
            couriers.append(courier)
        total_weight += package
    else:

        package -= courier
        total_weight += courier
        packages.append(package)


print(f"Total weight {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(x) for x in packages)}")

else:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} but there are no more packages to deliver.")
    print(*couriers)