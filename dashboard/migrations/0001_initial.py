# Generated by Django 3.2.3 on 2021-05-27 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.TextField()),
                ('website_address', models.TextField()),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_entry', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='passwordentry',
            index=models.Index(fields=['website_address'], name='dashboard_p_website_a9034f_idx'),
        ),
    ]