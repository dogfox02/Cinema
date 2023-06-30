from django.shortcuts import render, redirect
from authorization.models import User, movieScore
from .models import Movie
from .torrent import make_magnet_from_file


def all_things(request):
    movies = Movie.objects.all()
    return render(request, 'ListOfFilms.html', {'movies': movies, 'logged_in': False})


def all_films(request):
    movies = Movie.objects.filter(type=2)
    return render(request, 'ListOfFilms.html', {'movies': movies, 'logged_in': False})


def all_animes(request):
    movies = Movie.objects.filter(type=1)
    return render(request, 'ListOfFilms.html', {'movies': movies, 'logged_in': False})


def all_serials(request):
    movies = Movie.objects.filter(type=3)
    return render(request, 'ListOfFilms.html', {'movies': movies, 'logged_in': False})


def player(request, film_id):
    film = Movie.objects.get(pk=film_id)
    magnet = make_magnet_from_file(film_id)
    return render(request, 'player.html', {'film': film, 'magnet': magnet, 'logged_in': False})


def all_things_logged_in(request, user_id):
    user = User.objects.get(id=user_id)
    movies = Movie.objects.all()
    return render(request, 'ListOfFilms.html', {'movies': movies, 'user': user, 'logged_in': True})


def all_films_logged_in(request, user_id):
    user = User.objects.get(id=user_id)
    movies = Movie.objects.filter(type=2)
    return render(request, 'ListOfFilms.html', {'movies': movies, 'user': user, 'logged_in': True})


def all_animes_logged_in(request, user_id):
    user = User.objects.get(id=user_id)
    movies = Movie.objects.filter(type=1)
    return render(request, 'ListOfFilms.html', {'movies': movies, 'user': user, 'logged_in': True})


def all_serials_logged_in(request, user_id):
    user = User.objects.get(id=user_id)
    movies = Movie.objects.filter(type=3)
    return render(request, 'ListOfFilms.html', {'movies': movies, 'user': user, 'logged_in': True})


def player_logged_in(request, film_id, user_id):
    user = User.objects.get(id=user_id)
    film = Movie.objects.get(pk=film_id)
    magnet = make_magnet_from_file(film_id)
    return render(request, 'player.html', {'film': film, 'user': user, 'logged_in': True, 'magnet': magnet})


def total_score(request, film_id):
    if request.method == "POST":
        print('okey')
        score = request.POST["estimation"]
        movie = Movie.objects.get(pk=film_id)
        if movie.inter_score == None:
            movie.inter_score = float(score)
        else:
            movie.inter_score = movie.inter_score + float(score)
        if movie.NUsersEstimated == None:
            movie.NUsersEstimated = 1
        else:
            movie.NUsersEstimated += 1
        movie.movieTotalScore = movie.inter_score / movie.NUsersEstimated
        movie.save()
        print(movie.movieTotalScore)
    return redirect("http://127.0.0.1:8000/" + "movie/" + str(film_id))


def total_score(request, user_id, film_id):
    if request.method == "POST":
        score = request.POST["estimation"]
        movie = Movie.objects.get(pk=film_id)
        if movie.inter_score == None:
            movie.inter_score = float(score)
        else:
            movie.inter_score = movie.inter_score + float(score)
        if movie.NUsersEstimated == None:
            movie.NUsersEstimated = 1
        else:
            movie.NUsersEstimated += 1
        movie.movieTotalScore = movie.inter_score / movie.NUsersEstimated
        name = movie.name
        movie.save()
        movie_score = movieScore.objects.create_movie(film_id, name, score, user_id)
        #user = User.objects.get(pk=user_id)
        #user.movie = movie_score
        movie_score.save()

    return redirect("http://127.0.0.1:8000/" + str(user_id) + "/movie/" + str(film_id))


def all_search(request):
    if request.method == "POST":
        request_str = request.POST["search_request"]
        movies = Movie.objects.filter(name_lower__contains=request_str.lower())
    return render(request, 'ListOfFilms.html', {'movies': movies, 'logged_in': False})


def all_search_logged_in(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        request_str = request.POST["search_request"]
        movies = Movie.objects.filter(name_lower__contains=request_str.lower())
    return render(request, 'ListOfFilms.html', {'movies': movies, 'user': user, 'logged_in': True})
