from django import forms
from . import models


class PasswordEntryForm(forms.ModelForm):
    website_name = forms.CharField()
    website_address = forms.CharField(widget=forms.URLInput())
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = models.PasswordEntry
        fields = ['website_name', 'website_address', 'username', 'password']


class MasterPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.PasswordEntry
        fields = ['password']
