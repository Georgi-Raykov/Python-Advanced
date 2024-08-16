def cookbook(*args):
    menu = {}

    for packet in args:
        recipe_name = packet[0]
        cuisine = packet[1]
        ingredients = packet[2]
        if cuisine not in menu:
            menu[cuisine] = {recipe_name: []}
        menu[cuisine][recipe_name] = ingredients
    sorted_menu = sorted(menu.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for key, value in sorted_menu:
        result += f"{key} cuisine contains {len(value)} recipes:\n"
        sorted_value = sorted(value.items(), key=lambda x: x[0])
        for key, val in sorted_value:
            result += f" * {key} -> Ingredients: {', '.join(val)}\n"
    return result


print(cookbook(('Spaghetti Bolognese', 'Italian', ['spaghetti', 'tomato sauce', 'ground beef']),
               ('Margarita pizza', 'Italian', ['pizza dough', 'tomato sauce', 'mozzarella']),
               ('Tiramisu', 'Italian', ['ladyfingers', 'mascarpone', 'coffee']),
               ('Croissant', 'French', ['flour', 'butter', 'yeast']),
               ('Ratatouille', 'French', ['eggplant', 'zucchini', 'tomatoes'])))
print()
print(cookbook(('Pad Thai', 'Thai', ['rice noodles', 'shrimp', 'peanuts', 'bean sprouts', 'tamarind sauce'])))
print()
print(cookbook(('Spaghetti Bolognese', 'Italian', ['spaghetti', 'tomato sauce', 'ground beef']),
               ('Margarita pizza', 'Italian', ['pizza dough', 'tomato sauce', 'mozzarella']),
               ('Tiramisu', 'Italian', ['ladyfingers', 'mascarpone', 'coffee']),
               ('Croissant', 'French', ['flour', 'butter', 'yeast']),
               ('Ratatouille', 'French', ['eggplant', 'zucchini', 'tomatoes']),
               ('Sushi Rolls', 'Japanse', ['rice', 'nori', 'fish', 'vegetables']),
               ('Miso soup', 'Japanse', ['tofu', 'seaweed', 'green onions']),
               ('Guacamole', 'Mexican', ['avocado', 'tomato', 'onion', 'lime'])))
