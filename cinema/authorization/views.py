from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import registrationForm, log_inForm
from .models import User, movieScore


class ShowAvatar(DetailView):
    model = User
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_ava(self, log, pas):
        user = User.objects.get(login=log)
        if pas == user.password:
            return user.ava

    def get_email(self, log, pas):
        user = User.objects.get(login=log)
        if pas == user.password:
            return user.email

    def get_id(self, log, pas):
        user = User.objects.get(login=log)
        u_id = user.pk
        if pas == user.password:
            return u_id


def reg_form(request):
    if request.method == "POST":
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            login = form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            ava = form.cleaned_data.get("ava")
            print(ava)
            User.objects.create_user(login, password, email, ava)
            return redirect('http://127.0.0.1:8000/')
    else:
        form = registrationForm()
    return render(request, 'auth.html', {'form': form})

def log_in_form(request, self=None):
    if request.method == "POST":
        log_in = log_inForm(request.POST)
        if log_in.is_valid():
            login = log_in.cleaned_data.get("login")
            password = log_in.cleaned_data.get("password")
            u_id = ShowAvatar.get_id(self, login, password)
            return redirect('http://127.0.0.1:8000/' + str(u_id))
    else:
        log_in = log_inForm()
    return render(request, 'log_in.html', {'log_in': log_in})

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    #Movies = user.movie
    movies = movieScore.objects.filter(user_id=user_id).exclude(movie_name="movie_name")
    return render(request, 'profile.html', {'movies': movies, 'user': user, 'logged_in': True})
