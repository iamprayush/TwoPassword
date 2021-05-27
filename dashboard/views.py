from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from . import models
from . import forms


class HomeView(LoginRequiredMixin, generic.ListView):
    login_url = '/users/login/'

    model = models.PasswordEntry
    template_name = 'dashboard/home.html'
    context_object_name = 'password_entries'
    paginate_by = 5

    def get_queryset(self):
        result = models.PasswordEntry.objects.filter(
            master=self.request.user).order_by('website_name')
        return result


class ShowPasswordEntry(LoginRequiredMixin, generic.View):
    """
    Endpoint to reveal the password for a website entry.

    The password entry is only revealed if the user enters the correct master
    password. The validity is tracked via a boolean session variable called
    master_is_authenticated. If it is false, or not present, the user is
    redirected to a form to enter their password.
    """

    login_url = '/users/login/'

    def get(self, request, pk):
        if not request.session.get('master_is_authenticated'):
            return redirect(
                reverse('dashboard:master_password') +
                f'?next=/password_entry/{pk}/')

        context = {}

        password_entry_instance = get_object_or_404(models.PasswordEntry,
                                                    pk=pk)
        context['password_entry'] = password_entry_instance

        # We don't want the authentication to persist over more than one queries
        # to this endpoint so every time a successful call to this endpoint is
        # made, the authentication will be falsified. This will ensure that the
        # next time the user visits this page, they will be asked for the
        # password again.
        request.session['master_is_authenticated'] = False

        return render(request, 'dashboard/password_entry_show.html', context)


class CreatePasswordEntry(LoginRequiredMixin, generic.View):
    login_url = '/users/login/'

    def get(self, request):
        form = forms.PasswordEntryForm()
        return render(request, 'dashboard/password_entry_create.html', {'form': form})

    def post(self, request):
        form = forms.PasswordEntryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.master = request.user
            obj.save()
            return redirect(reverse('dashboard:home'))

        return render(request, 'dashboard/password_entry_create.html', {'form': form})


class DeletePasswordEntry(LoginRequiredMixin, generic.edit.DeleteView):
    login_url = '/users/login/'
    model = models.PasswordEntry
    template_name = 'dashboard/password_entry_delete_confirm.html'
    success_url = '/'


class MasterPassword(LoginRequiredMixin, generic.View):
    """
    Form that accepts and validates the master password for the currently
    logged in user.
    Correctly filling this form will enable the `master_is_authenticated`
    session boolean and the user will be able to access the website's password.

    NOTE: This URL is directly accessible (although not via the UI). It could be
    a design decision whether or not we should allow that. Ideally this endpoint
    should only be accessed via a redirect from the password_entry endpoint.
    """

    login_url = '/users/login/'

    def get(self, request):
        form = forms.MasterPasswordForm()
        return render(request, 'dashboard/master_password.html',
                      {'form': form})

    def post(self, request):
        form = forms.MasterPasswordForm(request.POST)
        entered_password = form.data.get('password')

        if request.user.check_password(entered_password):
            request.session['master_is_authenticated'] = True

            full_path = request.get_full_path()
            if '?next=' in full_path:
                next_url = request.get_full_path().split('?next=')[1]
                return redirect(next_url)
            return redirect(reverse('dashboard:home'))

        return render(request, 'dashboard/master_password.html',
                      {'form': form, 'error_message': 'Incorrect password.'})
