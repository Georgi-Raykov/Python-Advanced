from collections import deque

peoples = deque()
while True:

    client = input()
    if client == 'End':
        break

    if client == 'Paid':

        print('\n'.join(peoples))
        peoples.clear()
    else:

        peoples.append(client)

print(f"{len(peoples)} people remaining.")

