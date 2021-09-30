from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.home, name="home"),
    path('article/', views.article, name="article"),
    # path('category/', views.category, name="category"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # path('dashboard/submissions/', views.submissions, name="submissions"),
    path('dashboard/profile/', views.profile, name="profile"),
    path('logout/', views.logoutUser, name="logout"),


     # password change
    path('dashboard/password_change/', auth_views.PasswordChangeView.as_view (template_name='passwords/password_change.html'), name="password_change"),
    path('dashboard/password_change/done/', auth_views.PasswordChangeDoneView.as_view (template_name='passwords/password_change_done.html'), name="password_change_done"),
    # password change

    path('dashboard/edit/', views.edit_profile, name="edit_profile"),
    path('dashboard/i_edit/', views.login_edit_profile, name="login_edit_profile"),



    # password reset
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view (template_name='passwords/password_reset_form2.html'), name="password_reset_confirm"),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view (template_name='passwords/password_reset_done.html'), name="password_reset_done"),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view (template_name='passwords/password_reset_complete.html'), name="password_reset_complete"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='passwords/password_reset_form.html'), name="password_reset"),
    # password reset


    path('activate_user/<uidb64>/<token>/', views.activate_user, name="activate"),
    path('dashboard/submit/', views.submit_script, name="submit_script"),
]