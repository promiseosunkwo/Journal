# from datetime import datetime
from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# User = settings.AUTH_USER_MODEL
User = get_user_model()
# import datetime
from django.utils import timezone
# import uuid

class my_user(models.Model):
    is_email_verified = models.BooleanField(default=False)
    # is_user_active = models.BooleanField(default=False)
    # timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, blank=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username


class Work(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Title(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Author(models.Model):
    workplace = models.ForeignKey(Work, on_delete=models.CASCADE)
    jobtype = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

  
class Journal(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(default=True)
    description = models.TextField(default=False)
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ArticleType(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class SpecialIssue(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title




class Status(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title



class Manuscript(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    specialissue = models.ForeignKey(SpecialIssue, on_delete=models.CASCADE)
    articletype = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    abstract = models.TextField(max_length=1000)
    keywords = models.CharField(max_length=100)
    numberofpages = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    published_status = models.BooleanField(default=False)
    rand = models.IntegerField(default=True)


    def __str__(self):
        return self.title


class CoauthorList(models.Model):
    name = models.CharField(max_length=100, default=False)
    
    def __str__(self):
        return self.name


class CoAuthors(models.Model):
    author = models.ForeignKey(CoauthorList, on_delete=models.CASCADE, default=False)
    email = models.EmailField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    correspondingauthor = models.BooleanField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    affiliation = models.CharField(max_length=100)
    rand = models.IntegerField(default=True)
    
    # def __str__(self):
    #     return self.email


class Uploads(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    manuscriptword = models.FileField(upload_to='ms_word/')
    # manuscriptpdf = models.FileField(blank=True, null=True,upload_to='pdf/')
    # graphicabstract = models.FileField(blank=True, null=True,upload_to='graphic_abstract/')
    # supplementaryfiles = models.FileField(blank=True, null=True,upload_to='files/')
    # coverletter = models.FileField(blank=True, null=True,upload_to='files/')
    # figures = models.FileField(blank=True, null=True,upload_to='files/')
    rand = models.IntegerField(default=True)

    # def __str__(self):
    #     return self.manuscriptword


class publish(models.Model):
    published_year = models.IntegerField()
    published_volume = models.IntegerField()
    published_issue = models.IntegerField()
    published_page_start = models.IntegerField()
    published_page_end = models.IntegerField()
    published_abstract = models.TextField(max_length=3000)
    published_full_text = models.TextField(max_length=3000)
    published_pdf = models.FileField(upload_to='published/')
    published_status = models.BooleanField(default=False)
    rand = models.IntegerField(default=True)
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self. published_year)

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.published_pdf.url
    #     except:
    #         url = ''
    #     return url


class front_page(models.Model):
    slider1 = models.FileField(upload_to='frontpage/')
    slider2 = models.FileField(upload_to='frontpage/', default=True)
    slider3 = models.FileField(upload_to='frontpage/',default=True)
    logo = models.FileField(upload_to='frontpage/')
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    logo_text = models.TextField(max_length=100)

    def __str__(self):
        return str(self.email)

    @property
    def imageURL(self):
        try:
            url = self.slider1.url
            url = self.slider2.url
            url = self.slider3.url
        except:
            url = ''
        return url

  

    

