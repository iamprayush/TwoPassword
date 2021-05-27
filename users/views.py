from django.shortcuts import render
from django.views import View
from .forms import RegisterForm


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'users/register.html', {"form": form})


class Login(View):
    def get(self, request):
        return render(request, 'users/login.html')
