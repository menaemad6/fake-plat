# Generated by Django 4.1.7 on 2024-08-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0110_alter_transaction_purchase_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='buylesson',
            name='discount_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='buylesson',
            name='discount_value',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]