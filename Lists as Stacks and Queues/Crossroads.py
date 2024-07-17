from collections import deque

green_light_seconds = int(input())
free_window = int(input())
automobiles = deque()
passed_cars = []
crashed_place = ''
crashed_car = ''
is_crash = False
while True:

    if is_crash:
        print("A crash happened!")
        print(f"{crashed_car} was hit at {crashed_place}.")
        break

    current_green_seconds = green_light_seconds

    line = input()

    if line == 'END':
        print("Everyone is safe.")
        print(f"{len(passed_cars)} total cars passed the crossroads.")
        break
    if line != 'green':
        automobiles.append(line)


    else:

        while automobiles:
            car = automobiles.popleft()
            if len(car) <= current_green_seconds:
                current_green_seconds -= len(car)
                passed_cars.append(car)
            else:
                current_green_seconds = current_green_seconds + free_window
                if len(car) <= current_green_seconds:
                    passed_cars.append(car)
                    break
                else:
                    crashed_place = car[current_green_seconds]
                    crashed_car = car
                    is_crash = True
                    break
