def even_odd(*args):
    command = args[-1]

    primary = 0 if command == 'even' else 1

    result = [int(args[x]) for x in range(len(args) - 1) if int(args[x]) % 2 == primary]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))