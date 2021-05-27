from django import forms
from . import models


class MasterPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.PasswordEntry
        fields = ['password']
