# Generated by Django 4.1.7 on 2024-08-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0111_buylesson_discount_id_buylesson_discount_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='part_id',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
