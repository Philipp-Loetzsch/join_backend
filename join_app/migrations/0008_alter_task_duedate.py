# Generated by Django 5.1.6 on 2025-03-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0007_rename_custom_color_usercontact_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.IntegerField(),
        ),
    ]
