# from journal_app.models import Author
from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Author, my_user
# from .models import User



class CreateRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *arg, **kwargs):
        super(AuthorForm,self).__init__(*arg, **kwargs)
        self.fields['workplace'].empty_label = "Select"
        self.fields['jobtype'].empty_label = "Select"
        self.fields['title'].empty_label = "Select"
        self.fields['Country'].empty_label = "Select"
        # self.fields['user'].disabled = True
        

class my_userForm(forms.ModelForm):

    class Meta:
        model = my_user
        fields = '__all__'
        # exclude = ['user']

 