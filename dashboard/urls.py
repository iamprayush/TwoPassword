from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('master_password/',
         views.MasterPassword.as_view(),
         name='master_password'),
    path('password_entry/<pk>/',
         views.PasswordEntryView.as_view(),
         name='password_entry'),
]
