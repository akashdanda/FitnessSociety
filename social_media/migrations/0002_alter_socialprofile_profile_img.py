# Generated by Django 4.1.5 on 2023-02-24 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialprofile',
            name='profile_img',
            field=models.ImageField(default='static/images/profile_images/blankProfile.png', upload_to='static/images/profile_images'),
        ),
    ]
