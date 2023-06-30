from django.shortcuts import render
# Create your views here.
from django.views.generic import DetailView

from authorization.models import User


def home_id(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'home.html', {'user': user, 'logged_in': True})

def home(request):
    return render(request, 'home.html', {'logged_in': False})
