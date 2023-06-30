"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import all_films, all_animes, all_serials, all_things, player, all_things_logged_in, all_animes_logged_in, \
    all_serials_logged_in, all_films_logged_in, player_logged_in, all_search, all_search_logged_in

from . import views
from .views import all_films, all_animes, all_serials, all_things, player


urlpatterns = [
    path('look', all_things),
    path('animes', all_animes),
    path('serials', all_serials),
    path('films', all_films),
    path('movie/<int:film_id>', player),
    path('<int:user_id>/look', all_things_logged_in),
    path('<int:user_id>/animes', all_animes_logged_in),
    path('<int:user_id>/serials', all_serials_logged_in),
    path('<int:user_id>/films', all_films_logged_in),
    path('<int:user_id>/movie/<int:film_id>', player_logged_in),
    path('movie/<int:film_id>/estimate', views.total_score),
    path('<int:user_id>/movie/<int:film_id>/estimate', views.total_score),
    path('search', all_search),
    path('<int:user_id>/search', all_search_logged_in),
]
