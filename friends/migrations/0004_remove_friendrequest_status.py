# Generated by Django 4.1.5 on 2023-03-15 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='status',
        ),
    ]
