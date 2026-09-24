import math

def average_rating(movies):
    """
    Возвращает среднюю оценку по каталогу с округлением до одного знака
    """ 
    sum_rating = sum(movie["rating"] for movie in movies)
    av_rating = sum_rating/len(movies)
    return round(av_rating, 1)

def catalog_age_stats(movies, current_year=2026):
    """
    Возвращает кортеж (самый старый фильм в годах, самых новый фильм в годах, среднее)
    с округлением вверх
    """
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
    """
    Переревод минут в формат "Xч Yм", используя целочисленное деление и остаток от деления
    """
    movie_hours = minutes // 60
    movie_minutes = minutes % 60
    return movie_hours, movie_minutes

def rating_tier(rating):
    return "шедевр" if rating >= 9 else "хорошо" if rating >= 7 else "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"
 
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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

print('Средний рейтинг фильмов по каталогу', average_rating(movies))
print('Лет самому старому, самому новому и в среднем фильмам в каталоге соответственно:', catalog_age_stats(movies))
print('Длительность фильма The Dune Chronicles:', duration_in_hours(movies[0]["duration_min"]))
print('Согласно рейтингу фильм входит в категорию', rating_tier(movies[0]["rating"]))
print('Согласно году выходы фильм входит в категорию', decade_label(movies[0]["year"]))