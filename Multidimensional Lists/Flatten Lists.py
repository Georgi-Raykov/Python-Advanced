text = input().split('|')
result = []
for i in range(len(text) -1, -1, -1):

    result.append(text[i].strip())
print(' '.join(result))
