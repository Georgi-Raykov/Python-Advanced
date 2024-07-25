from collections import deque

text = deque(input().split())
main = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]
collected_colors = []

while text:

    if len(text) == 1:

        last_substring = text.pop()
        if last_substring in main:
            collected_colors.append(last_substring)
            break
        else:
            break

    first = text.popleft()
    last = text.pop()

    result = first + last

    if result in main or result in secondary:
        collected_colors.append(result)
        continue
    result = last + first
    if result in main or result in secondary:
        collected_colors.append(result)
        continue

    first = first[:-1]
    last = last[:-1]
    if first:
        text.insert(len(text) // 2, first)
    if last:
        text.insert(len(text) // 2, last)

form_secondary_color = {'orange': ['red', 'yellow'],
                        'purple': ['red', 'blue'],
                        'green': ['yellow', 'blue']}

result = []

for color in collected_colors:

    if color in main:
        result.append(color)
        continue
    is_forming = True
    for forming_color in form_secondary_color[color]:

        if forming_color not in collected_colors:
            is_forming = False
            break
    if is_forming:
        result.append(color)

print(result)
