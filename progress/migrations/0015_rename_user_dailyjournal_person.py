# Generated by Django 4.1 on 2023-01-12 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0014_alter_calorietracker_user_alter_workoutmodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyjournal',
            old_name='user',
            new_name='person',
        ),
    ]
