# Generated by Django 5.1.6 on 2025-03-18 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
    ]
