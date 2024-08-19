def team_lineup(*args):
    collected_teams = {}
    for item in args:

        name = item[0]
        country = item[1]

        if country not in collected_teams:
            collected_teams[country] = []
        collected_teams[country].append(f" -{name}")
    result = ''
    sorted_collection = sorted(collected_teams.items(), key=lambda x: (-len(x[1]), x[0]))

    for country, names in sorted_collection:
        result += f"{country}:\n" + '\n'.join(names) + '\n'
    return result


print(team_lineup(("Harry Kane", "England"), ("Manuel Neuer", "Germany"), ("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"), ("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany")))
print()
print(team_lineup(("Lionel Messi", "Argentina"), ("Neymar", "Brazil"), ("Cristiano Ronaldo", "Portugal"),
                  ("Harry Kane", "England"), ("Kylian Mbappe", "France"), ("Raheem Sterling", "England")))
print()
print(team_lineup(("Harry Kane", "England"), ("Manuel Neuer", "Germany"), ("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"), ("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany"),
                  ("Bruno Fernandes", "Portugal"), ("Bernardo Silva", "Portugal"), ("Harry Maguire", "England")))
