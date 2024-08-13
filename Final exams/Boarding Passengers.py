def boarding_passengers(capacity, *args):
    all_passengers = {}

    for guests, benefit in args:
        if capacity > 0 and capacity >= guests:
            capacity -= guests

            if benefit not in all_passengers:
                all_passengers[benefit] = 0
            all_passengers[benefit] += guests

        else:
            continue
    result = ''
    sorted_boarding = sorted(all_passengers.items(), key=lambda x: (-x[1], x[0]))

    for benefit, guests in sorted_boarding:
        result += f"## {benefit}: {guests} guests\n"
    if len(all_passengers) == len(args):
        result += "all passengers are successfully boarded!"
    elif capacity == 0 and len(all_passengers) < len(args):
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    elif capacity > 0 and len(args) > len(all_passengers):
        result += f"Partial boarding completed. Available capacity {capacity}"

    print("Boarding details by benefit plan:")
    return ''.join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print()
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'),
                          (31, 'Platinum'), (20, 'Diamond')))
print()
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'),
                          (10, 'Gold')))
