# Generated by Django 4.1 on 2023-01-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0003_alter_workoutmodel_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutmodel',
            name='Description',
        ),
        migrations.AddField(
            model_name='workoutmodel',
            name='Quick_Description',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
