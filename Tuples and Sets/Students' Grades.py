n = int(input())
info = {}
for _ in range(n):

    name, grade = input().split()

    if name not in info:

        info[name] = []

    info[name].append(float(grade))

for name, grades in info.items():

    average = sum(grades) / len(grades)
    grade_list = [str(f"{grade:.2f}") for grade in grades]
    print(f"{name} -> {' '.join(grade_list)} ({average:.2f})")
