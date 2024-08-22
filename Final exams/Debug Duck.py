from collections import deque

programmers_time = deque(int(x) for x in input().split())
tasks = deque(int(x) for x in input().split())
results = {'Darth Vader Ducky': 0, 'Thor Ducky': 0, 'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}
while programmers_time and tasks:
    time = programmers_time.popleft()
    task = tasks.pop()
    number = time * task

    if 0 <= number <= 60:
        results['Darth Vader Ducky'] += 1
    elif 61 <= number <= 120:
        results['Thor Ducky'] += 1
    elif 121 <= number <= 180:
        results['Big Blue Rubber Ducky'] += 1
    elif 181 <= number <= 240:
        results['Small Yellow Rubber Ducky'] += 1
    else:
        task -= 2
        tasks.append(task)
        programmers_time.append(time)

print("Congratulation, all tasks have been completed! Rubber ducks rewarded:")
for key, value in results.items():
    print(f"{key}: {value}")

# input 1

# 10 15 12 18 22 6
# 12 16 5 6 9 1

# input 2

# 2 55 17 31 23
# 7 5 17 4 27
