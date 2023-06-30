from django import forms
from .models import User


class registrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["login", "email", "ava"]
        labels = {'login': "Логин", 'password': "Пароль", 'password2': "Повторите пароль",
                  'email': "Электронная почта", 'ava': "Аватар"}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class log_inForm(forms.ModelForm):
   class Meta:
        model = User
        fields = ["login", "password"]
        labels = {'login': "Логин", 'password': "Пароль"}