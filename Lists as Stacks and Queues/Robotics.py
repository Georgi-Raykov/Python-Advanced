from collections import deque


def input_robots():
    result = {}

    line = input().split(';')
    for input_robot in line:
        robot_details = input_robot.split('-')
        name = robot_details[0]
        time = int(robot_details[1])
        result[name] = time

    return result


def read_products():
    result = deque()
    while True:

        line = input()
        if line == 'End':
            break
        result.append(line)
    return result


def to_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


robots = input_robots()
available_robots = [x for x in robots.keys()]
processing_robots = {}
starting_time = [int(x) for x in input().split(':')]

time_to_seconds = to_seconds(starting_time[0], starting_time[1], starting_time[2])

products = read_products()


def time_to_str(time_to_seconds):
    hours = time_to_seconds // 3600
    minutes = (time_to_seconds % 3600) // 60
    seconds = (time_to_seconds % 3600) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


while products:
    time_to_seconds = (time_to_seconds + 1) % (24 * 60 * 60)

    for robot_name in [x for x in processing_robots.keys()]:

        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] == 0:
            processing_robots.pop(robot_name)
    product = products.popleft()

    for robot in available_robots:
        if robot not in processing_robots:
            print(f"{robot} - {product} [{time_to_str(time_to_seconds)}]")
            processing_robots[robot] = robots[robot]
            break
    else:

        products.append(product)
