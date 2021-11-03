from django.contrib import admin
from .models import ArticleType, Journal, Manuscript,CoauthorList, CoAuthors, Uploads, SpecialIssue, Work,Job,Title,Country,Author,my_user,Status,publish,front_page



# class COAuthorsAdmin(admin.TabularInline):
#     model = CoAuthors

class Coauthorinline(admin.TabularInline):
    model = CoAuthors

class CoauthorListAdmin(admin.ModelAdmin):
    inlines = [Coauthorinline]


admin.site.register(Work)
admin.site.register(Job)
admin.site.register(Title)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(my_user)
admin.site.register(Manuscript)
admin.site.register(Status)
admin.site.register(Uploads)
admin.site.register(Journal)
admin.site.register(ArticleType)
admin.site.register(SpecialIssue)
admin.site.register(CoauthorList,CoauthorListAdmin)
admin.site.register(publish)
admin.site.register(front_page)