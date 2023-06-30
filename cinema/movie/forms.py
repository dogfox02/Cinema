from django import forms
from .models import Movie

class movieScore_form(forms.Form):
    CHOICES = (('1', '1'), ('2', '2'), ('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),)
    field = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Movie
        fields = ["score"]