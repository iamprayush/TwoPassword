from django.db import models
from django.contrib.auth.models import User


class PasswordEntry(models.Model):
    master = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='password_entry')
    website_name = models.TextField()
    website_address = models.TextField()
    username = models.TextField()
    password = models.TextField()

    class Meta:
        # Indexing on website address since it is used as a search parameter.
        indexes = [models.Index(fields=['website_address'])]

    def __str__(self):
        return f'Password entry for {self.website_name}.'
