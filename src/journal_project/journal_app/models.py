from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# User = settings.AUTH_USER_MODEL
User = get_user_model()

class my_user(models.Model):
    is_email_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, blank=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)


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

  
