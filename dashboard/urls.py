from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('master_password/',
         views.MasterPassword.as_view(),
         name='master_password'),
     path('password_entry/',
         views.CreatePasswordEntry.as_view(),
         name='create_password_entry'),
    path('password_entry/<pk>/',
         views.ShowPasswordEntry.as_view(),
         name='show_password_entry'),
    path('password_entry/<pk>/delete/',
         views.DeletePasswordEntry.as_view(),
         name='delete_password_entry'),
]
