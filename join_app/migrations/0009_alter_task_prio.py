# Generated by Django 5.1.6 on 2025-03-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0008_alter_task_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prio',
            field=models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('urgent', 'urgent')], max_length=20),
        ),
    ]
