# Generated by Django 4.1.7 on 2024-08-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0072_remove_groupmember_group_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='message_image',
            field=models.ImageField(blank=True, null=True, upload_to='groups_images'),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='image',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='group_images'),
        ),
    ]
