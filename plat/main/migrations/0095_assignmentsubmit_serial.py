# Generated by Django 4.1.7 on 2024-08-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0094_assignmentsubmit_true_answers_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmit',
            name='serial',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]