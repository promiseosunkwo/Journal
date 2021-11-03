# from journal_app.models import Author
from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Manuscript, my_user, CoauthorList, Uploads,CoAuthors,publish
from django.forms import modelformset_factory
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
#  message = forms.CharField(widget=forms.Textarea)


 
class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = '__all__'
        exclude = ('author','date_added','rand','status','published_status')

class ManuscriptFormEditor(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = '__all__'
        exclude = ('author','date_added','rand','published_status')
       

# this table is to get the main author of inline form associated with submitting a manuscript
class CoauthorListAuthor(forms.ModelForm):
        class Meta:
                model = CoauthorList
                fields = ('__all__')


# this table is to get the co author in an inline format when submitting a manuscript
class CoauthorListForm(forms.ModelForm):
    class Meta:
        model = CoAuthors
        fields = ( "email","firstname","lastname","correspondingauthor","country","affiliation")
        # exclude = ('rand',)


# this table is the form factory inline format
CoauthorFormset = inlineformset_factory(
    CoauthorList,
    CoAuthors,
    CoauthorListForm,
    extra=0,
    can_delete = True
    # min_num=1

)




class UploadsForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'
        exclude = ('author','date_added','rand')
        # exclude = []

class publishForm(forms.ModelForm):
    class Meta:
        model = publish
        fields = '__all__'
        exclude = ('published_status','rand','date_published')
        # exclude = []

# coauthor_formset = modelformset_factory(
#     CoAuthors, fields=("email", "firstname","lastname","correspondingauthor", "country", "affiliation"), extra=0
#     ) 