# Generated by Django 4.2.9 on 2024-01-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='static/images/user.png', null=True, upload_to='profile_images', verbose_name='Profile Pic'),
        ),
    ]
