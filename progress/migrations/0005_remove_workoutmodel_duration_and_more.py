# Generated by Django 4.1 on 2023-01-04 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0004_remove_workoutmodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutmodel',
            name='Duration',
        ),
        migrations.AddField(
            model_name='workoutmodel',
            name='Duration_Hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='workoutmodel',
            name='Mood',
            field=models.CharField(choices=[('ENERGIZED', 'energized'), ('EXCITED', 'excited'), ('FATIGUED', 'fatigued'), ('STRESSED', 'stressed'), ('CALM', 'calm'), ('SAD', 'sad')], max_length=9),
        ),
    ]
