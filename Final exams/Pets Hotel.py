def accommodate_new_pets(capacity, max_weight, *args):
    accommodated_pets = {}
    all_accommodation_pets = [x for x in args if float(x[1] < max_weight)]
    pets = 0
    for item in args:

        type_pet = item[0]
        weight = float(item[1])

        if type_pet not in accommodated_pets and capacity > 0 and weight < max_weight:
            accommodated_pets[type_pet] = []
            accommodated_pets[type_pet].append(type_pet)
            pets += 1
            capacity -= 1
        elif type_pet in accommodated_pets and capacity > 0 and weight < max_weight:
            accommodated_pets[type_pet].append(type_pet)
            pets += 1
            capacity -= 1
        if capacity == 0:
            break
    sorted_accommodated_pets = sorted(accommodated_pets.items(), key=lambda x: x[0])
    result = ''
    if pets == len(all_accommodation_pets):
        result += f"All pets are accommodated! Available capacity: {capacity}\n"
    else:
        result += "You did not manage to accommodate all pets!\n"
    for key, value in sorted_accommodated_pets:
        result += f"{key}: {len(value)}\n"
    return result


print(accommodate_new_pets(10, 15.0, ('cat', 5.8), ('dog', 10.0)))
print()
print(accommodate_new_pets(10, 10.0, ('cat', 5.8), ('dog', 10.5), ('parrot', 0.8), ('cat', 3.1)))
print()
print(accommodate_new_pets(2, 15.0, ('dog', 10.0), ('cat', 5.8), ('cat', 2.7)))
