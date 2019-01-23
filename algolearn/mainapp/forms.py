from django import forms
import datetime


class UserForm(forms.Form):
    login = forms.CharField()
    name = forms.CharField()
    surname = forms.CharField()
    patronymic = forms.CharField()
    email=forms.EmailField()
    birthdate=forms.DateTimeField()
    todaydate=datetime.datetime.now()
    status=forms.CheckboxInput()
    admin=forms.BooleanField()
    password=forms.PasswordInput()


