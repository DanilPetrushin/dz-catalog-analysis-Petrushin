import math


### ЭТАП 1. РАЗМИНКА: ПЕРЕМЕННЫЕ, ЧИСЛА, MATH
def average_rating(movies):
    sum_rating = sum(movie["rating"] for movie in movies)
    av_rating = sum_rating/len(movies)
    return round(av_rating, 1)

def catalog_age_stats(movies, current_year=2026):
    oldest_movie = 0
    newest_movie = 200
    ages_total = 0
    for movie in movies:
        if current_year - movie["year"] >= oldest_movie:
            oldest_movie = current_year - movie["year"]
        if current_year - movie["year"] <= newest_movie:
                newest_movie = current_year - movie["year"]
        ages_total += current_year - movie["year"]
    average_movie = math.ceil(ages_total/len(movies))
    return oldest_movie, newest_movie, average_movie

def duration_in_hours(minutes):
    movie_hours = minutes // 60
    movie_minutes = minutes % 60
    return movie_hours, movie_minutes

### ЭТАП 2. УСЛОВИЯ И MATCH
def rating_tier(rating):
    return "шедевр" if rating >= 9 else "хорошо" if rating >= 7 else "средне" if rating >= 5 else "слабо" #noqa: E501

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

### ЭТАП 3. ЦИКЛЫ 
def count_long_movies(movies, threshold=120):
    i = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            i += 1
    return i 

### ЭТАП 4. СТРОКИ
def normalize_title(title):
    title = title.split()
    all_phrase = []
    for word in title:
        phrase = word[0].upper() + word[1:].lower() 
        all_phrase.append(phrase)
        #В качестве альтернативы двум верхним строкам можно использовать
        #all_phrase.append(word.capitalize()) 
    return " ".join(all_phrase).lstrip().rstrip()

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    hours, minutes = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    phrase = (f'{normalize_title(movie["title"])} ({movie["year"]}) '
              f'— {movie["rating"]}/10, {hours}ч {minutes}м, жанры: {genres}')
    return phrase

### ЭТАП 5. СПИСКИ
def titles_sorted_by_rating(movies):
    movies_sorted = sorted(movies, key = lambda movie: movie["rating"], reverse = True)
    return[movie["title"] for movie in movies_sorted]

def top_n_by_rating(movies, n=3):
    movies_sorted = sorted(movies, key = lambda movie: movie["rating"], reverse = True)
    return [(movie["title"], movie["rating"]) for movie in movies_sorted[:n]]

### ЭТАП 6. СЛОВАРИ
def count_by_genre(movies):
    genre_dictionary = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_dictionary[genre] = genre_dictionary.get(genre,0) + 1
    return genre_dictionary

def actor_filmography(movies):
    actor_dictionary = {}
    for movie in movies:
        for actor in movie["actors"]:
                if actor not in actor_dictionary:
                    actor_dictionary[actor] = []
                actor_dictionary[actor].append(movie["title"])
    return actor_dictionary

### ЭТАП 7. МНОЖЕСТВА
def all_genres(movies):
    unique_genres = set()
    for movie in movies:
        unique_genres = unique_genres | movie["genres"]
    return unique_genres

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    genres_b = set()
    for movie in movies_a:
        genres_a = genres_a | movie["genres"]
    for movie in movies_b:
        genres_b = genres_b | movie["genres"]    
    return genres_a - genres_b

### ЭТАП 8. ИТЕРАТОРЫ И ГЕНЕРАТОРЫ
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

### ЭТАП 9. ИТОГОВЫЙ ОТЧЁТ
def build_report(movies):
    x, x, average_age  = catalog_age_stats(movies) 
    print('ОТЧЁТ ПО КАТАЛОГУ')
    print('Средний рейтинг', average_rating(movies))
    print('Средний возраст фильмов:', average_age)
    print('\nТоп-3 фильма:')
    for title, rating in top_n_by_rating(movies):
        for movie in movies:
            if movie["title"] == title:
                print(" ", format_report_line(movie))
    print("\nФильмов по жанрам:")
    genre_counter = count_by_genre(movies)
    for genre in genre_counter:
        print(" ", genre, "—", genre_counter.get(genre, 0))
    print("\nВсе жанры каталога:", ', '.join(sorted(all_genres(movies))))
    

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, #noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

### ЭТАП 3. ЦИКЛЫ 
# for movie in movies: 
#     comedy = 0
#     for genres in movie["genres"]:
#         if genres == 'comedy':
#             comedy = 1
#     if comedy == 1:
#         continue
#     else:
#         print(movie['title'])

# i = 0
# while i < len(movies):
#     if movies[i]['rating'] > 9:
#         print(movies[i]['title'], ' - шедевр')
#         break
#     i += 1
# else:
#     print('Шедевров не найдено')

### ЭТАП 6. СЛОВАРИ
# above_average_rating = {movie["title"]: movie["rating"] 
# for movie in movies if movie["rating"] > average_rating(movies)}
# print(above_average_rating)

### ЭТАП 7. ИТЕРАТОРЫ И ГЕНЕРАТОРЫ
# for movie in iter_high_rated(movies):
#     print(format_report_line(movie))
# print(sum(movie["duration_min"] for movie in movies if movie["rating"] > 7))

### ЭТАП 9. ИТОГОВЫЙ ОТЧЁТ
build_report(movies)