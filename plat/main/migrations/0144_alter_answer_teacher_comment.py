# Generated by Django 4.1.7 on 2024-10-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0143_answer_teacher_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='teacher_comment',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
    ]
