from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.Home.as_view(), name='dashboard_home_view'),
    path('password_entry/<pk>/',
         views.PasswordEntryDetailView.as_view(),
         name='password_entry_detail_view'),
]
