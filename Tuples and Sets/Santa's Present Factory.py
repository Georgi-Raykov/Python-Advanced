from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

crafts = {150: 'Doll',
          250: 'Wooden train',
          300: 'Teddy bear',
          400: 'Bicycle'}

crafted = {}

while materials and magic_level:

    material = materials.pop()
    magic = magic_level.popleft()

    if material == 0 and magic == 0:
        continue
    elif material == 0:
        magic_level.appendleft(magic)
        continue
    elif magic == 0:
        materials.append(material)
        continue

    operation = material * magic

    if operation < 0:
        result = material + magic
        materials.append(result)
        continue

    if operation in crafts:
        if crafts[operation] not in crafted:
            crafted[crafts[operation]] = 0

        crafted[crafts[operation]] += 1
    else:
        material += 15
        materials.append(material)
if 'Doll' and 'Train' in crafted or 'Teddy bear' and 'Bicycle' in crafted:

    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    magic_level = reversed(magic_level)
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in sorted(crafted.items()):
    print(f"{key}: {value}")
