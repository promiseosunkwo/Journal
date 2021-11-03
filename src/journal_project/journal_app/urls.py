from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# from .forms import ManuscriptForm,CoAuthorsForm,UploadsForm
# from .views import SubmitWizard


urlpatterns = [
    path('', views.home, name="home"),
    path('article/<int:rand>/', views.article, name="article"),
    # path('category/', views.category, name="category"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('all/', views.all_articles, name="all"),
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
    path('dashboard/display/', views.display_script, name="display_script"),
    path('dashboard/submit/', views.submit_script, name="submit_script"),
    path('delete<int:rand>/', views.delete_script, name="delete_script"),
    path('<int:id>/', views.delete_user, name="delete_user"),
    path('dashboard/update/<int:rand>/', views.edit_script, name="edit_script"),


    path('editor/overview/', views.editor_overview, name="editor_overview"),    
    path('editor/pending/', views.pending_journals, name="pending_journals"), 
    path('editor/accepted/', views.accepted_journals, name="accepted_journals"),
    path('editor/rejected/', views.rejected_journals, name="rejected_journals"),
    path('editor/review/', views.inreview_journals, name="inreview_journals"),
    path('editor/revision/', views.revision_journals, name="revision_journals"),
    path('editor/all_users/', views.all_users, name="all_users"),

    path('editor/full_details/<int:rand>/', views.full_details, name="full_details"),

    path('editor/all_users/<int:id>/', views.disable_user, name="disable"),


    path('editor/publish/<int:rand>/', views.publish_journal, name="publish"),

    path('editor/published/', views.all_published, name="all_published"),



    path('journal/<int:id>/', views.journal_page, name="journal"),

    

]