from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('article/', views.article, name="article"),
    # path('category/', views.category, name="category"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    # path('dashboard/', views.dashboard, name="dashboard"),
    # path('dashboard/submissions/', views.submissions, name="submissions"),
    # path('dashboard/profile/', views.profile, name="profile"),
    # path('dashboard/password/', views.change_password, name="change_password"),
]