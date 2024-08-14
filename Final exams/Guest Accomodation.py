
def accommodate(*args, **kwargs):
    un_accommodate_guests = 0
    accommodate_guests = {}
    for guests in args:
        is_find = False
        while len(kwargs):
            for key, value in kwargs.items():
                item, room_number = key.split('_')
                if guests == value:
                    accommodate_guests[room_number] = guests
                    kwargs.pop(key)
                    is_find = True
                    break
            if is_find:
                break
            else:
                for key, value in kwargs.items():
                    item, room_number = key.split('_')
                    if guests < value:
                        accommodate_guests[room_number] = guests
                        kwargs.pop(key)
                        is_find = True
                        break
            if is_find:
                break
            else:
                un_accommodate_guests += guests
                break
    result = ''
    if accommodate_guests:
        sorted_accommodate = sorted(accommodate_guests.items(), key=lambda x: x[1])
        result += f"A total of {len(accommodate_guests)} accommodations were completed!\n"
        for room, guests in sorted_accommodate:
            result += f"<Room {room} accommodates {guests} guests>\n"
        if un_accommodate_guests:
            result += f"Guests with no accommodation: {un_accommodate_guests}\n"
        if kwargs:
            result += f"Empty rooms: {len(kwargs)}"
    else:
        result += f"No accommodations were completed!\n" \
                  f"Guests with no accommodation: {un_accommodate_guests}\n" \
                  f"Empty rooms: {len(kwargs)}"
    return result


# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
# print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
