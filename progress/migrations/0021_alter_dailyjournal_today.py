# Generated by Django 4.1.5 on 2023-03-08 07:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0020_alter_dailyjournal_upload_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyjournal',
            name='today',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
