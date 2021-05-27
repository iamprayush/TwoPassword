from django.shortcuts import render
from django.views import View

class Register(View):
    def get(self, request):
        return render(request, 'users/register.html')
    
    def post(self, request):
        pass

class Login(View):
    def get(self, request):
        return render(request, 'users/login.html')
