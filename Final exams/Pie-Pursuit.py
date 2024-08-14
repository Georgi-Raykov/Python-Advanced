from collections import deque

pie_content = deque(int(x) for x in input().split())
pies = deque(int(x) for x in input().split())

while pie_content and pies:

    content = pie_content.popleft()
    pie = pies.pop()

    if content < pie:
        pie -= content
        if pie == 1 and len(pies) > 0:
            pies[-1] += 1
        else:
            pies.append(pie)
    elif content > pie:
        content -= pie
        pie_content.append(content)
if pie_content:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in pie_content)}")
elif pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")
else:
    print("We have a champion!")