text = input()

result = {}

for i in text:

    if i not in result:

        result[i] = 0

    result[i] += 1

for key, value in sorted(result.items()):

    print(f"{key}: {value} time/s")