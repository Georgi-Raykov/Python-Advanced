def draw_cards(*args, **kwargs):
    monsters = []
    spells = []

    for card_name, type_card in args:

        if type_card == 'monster':
            monsters.append(f" ***{card_name}")
        else:
            spells.append(f" $$${card_name}")
    for card_name, type_card in kwargs.items():

        if type_card == 'monster':
            monsters.append(f" ***{card_name}")
        else:
            spells.append(f" $$${card_name}")
    result = ''
    if monsters:
        result += "Monster cards:\n" + '\n'.join(sorted(monsters, reverse=True))
    if spells:
        result += "\nSpell cards:\n" + '\n'.join(sorted(spells))

    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell"))
# print(draw_cards(("celtic guardian", "monster"), ('earthquake', 'spell'), ('fireball', 'spell'),
# raigeki="spell", destroy='spell'))
