from django.shortcuts import render


def home(request):
    context = {}

    return render(request, "index.html", context)


def article(request):
    context = {}

    return render(request, "article.html", context)



def register(request):
    context = {}

    return render(request, "register.html", context)


def loginPage(request):
    context = {}

    return render(request, "login.html", context)

