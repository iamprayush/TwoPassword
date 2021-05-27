from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .forms import RegisterForm


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:home'))

        return render(request, 'users/register.html', {'form': form})
