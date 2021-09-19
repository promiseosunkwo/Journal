# from journal_app.models import Author
from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    institute = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone','address','institute','email','password1','password2']

        

# class CreateRegisterForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['username','firstname','lastname','phone','address','institute','email','password1','password2']