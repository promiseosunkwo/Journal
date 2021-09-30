from django.contrib import admin
from .models import Work,Job,Title,Country,Author,my_user

# Register your models here.
admin.site.register(Work)
admin.site.register(Job)
admin.site.register(Title)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(my_user)