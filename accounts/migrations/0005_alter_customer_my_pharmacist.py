# Generated by Django 4.2.7 on 2023-11-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_customer_my_pharmacist_customer_my_pharmacist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='my_pharmacist',
            field=models.ManyToManyField(blank=True, related_name='my_customers', to='accounts.pharmacist'),
        ),
    ]
