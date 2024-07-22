from collections import deque

numbers = deque(int(x) for x in input().split())
target = int(input())

while True:

    if len(numbers) == 0 or len(numbers) == 1:
        break
    number = 0
    first_number = numbers.popleft()
    for num in numbers:
        if first_number + num == target:
            number = num
            print(f"{first_number} + {number} = {first_number + number}")
            numbers.remove(number)
            break
