# Generated by Django 4.1.7 on 2023-10-23 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_part_assignment_total_applicants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='assignment_questions_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='part',
            name='assignment_total_applicants',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentpartobject',
            name='assignment_questions_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentpartobject',
            name='assignment_total_applicants',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentpartobject',
            name='assignment_user_percentage',
            field=models.IntegerField(default=0),
        ),
    ]