n = int(input())
guests = set()
arrival_guests = set()
for _ in range(n):
    guest = input()
    guests.add(guest)

arrival = input()

while arrival != 'END':
    arrival_guests.add(arrival)
    arrival = input()

missing_guests = guests - arrival_guests

missing_vips = set(guest for guest in missing_guests if guest[0].isdigit())
missing_regular = missing_guests - missing_vips

print(len(missing_guests))

for vip in sorted(missing_vips):
    print(vip)
for regular in sorted(missing_regular):
    print(regular)