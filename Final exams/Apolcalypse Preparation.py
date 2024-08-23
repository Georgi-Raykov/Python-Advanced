from collections import deque

textile = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())
all_items = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}
while textile and medicaments:

    txt = textile.popleft()
    medic = medicaments.pop()
    result = txt + medic

    if result == 30:

        all_items['Patch'] += 1
    elif result == 40:
        all_items['Bandage'] += 1
    elif result == 100:
        all_items['MedKit'] += 1

    elif result > 100:
        all_items['MedKit'] += 1
        result -= 100
        medicaments[-1] += result
    else:
        medic += 10
        medicaments.append(medic)

if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textile:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_all_items = sorted(all_items.items(), key=lambda x: (-x[1], x[0]))

for key, value in sorted_all_items:
    if value > 0:
        print(f"{key} - {value}")
if textile:
    print(f"Textiles: {', '.join(str(x) for x in textile)}")
if medicaments:
    print(f"Medicaments: {', '.join(str(x) for x in medicaments)}")

# input 1

# 20 10 40 70 20
# 10 50 10 30 20 80

# input 2

# 30 30 10 80 60
# 40 20 30 10 70

# input 3

# 60 15 20 30 20
# 20 15 40
