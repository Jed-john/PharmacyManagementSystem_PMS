# Generated by Django 4.2.7 on 2023-11-20 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customer_user_alter_pharmacist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='my_pharmacist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.pharmacist'),
        ),
    ]
