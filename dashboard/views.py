from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class Home(LoginRequiredMixin, generic.ListView):
    login_url = '/users/login/'

    model = models.PasswordEntry
    template_name = 'dashboard/home.html'
    context_object_name = 'password_entries'
    paginate_by = 5
    
    def get_queryset(self):
        result = models.PasswordEntry.objects.filter(
            master=self.request.user).order_by('website_name')
        return result


class PasswordEntryDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/users/login/'

    model = models.PasswordEntry
    template_name = 'dashboard/password_entry_detail.html'
    context_object_name = 'password_entry'
