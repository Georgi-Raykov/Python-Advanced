def movie_organizer(*args):
    movies = {}

    for items in args:

        movie = items[0]
        genre = items[1]

        if genre not in movies:
            movies[genre] = []
        movies[genre].append(f"* {movie}")
    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for key, value in sorted_movies:
        result += f"{key} - {len(value)}\n" + '\n'.join(sorted(value)) + '\n'
    return result


print(movie_organizer(('The Matrix', 'Sci-fi')))
print()
print(movie_organizer(('The Godfather', 'Drama'), ('The Hangover', 'Comedy'),
                      ('The Shawshank Redemption', 'Drama'),
                      ('The Pursuit of Happiness', 'Drama'), ('The Hangover Part II', 'Comedy')))
print()
print(movie_organizer(('Avatar: The Way of Water', 'Action'), ('House of Gucci', 'Drama'),
                      ('Top Gun', 'Action'),
                      ('Ted', 'Comedy'), ('Duck Soup', 'Comedy'), ('The Dark Knight', 'Action'),
                      ('A Star is Born', 'Musicals'), ('The Warrior', 'Action'),
                      ('Like A Boss', 'Comedy'), ('The Green Mile', 'Drama'), ('21 Jump Street', 'Comedy')))