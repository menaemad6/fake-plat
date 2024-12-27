# Generated by Django 4.1.7 on 2024-07-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_platformsettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='platformsettings',
            options={'verbose_name': 'PLATFORM SETTINGS', 'verbose_name_plural': 'PLATFORM SETTINGS'},
        ),
        migrations.RenameField(
            model_name='platformsettings',
            old_name='name',
            new_name='text_logo',
        ),
        migrations.RemoveField(
            model_name='platformsettings',
            name='image',
        ),
        migrations.AddField(
            model_name='platformsettings',
            name='image_logo',
            field=models.ImageField(default='blank-lecture.jpeg', upload_to='platform_images'),
        ),
    ]