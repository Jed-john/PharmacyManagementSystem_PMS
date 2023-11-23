# Generated by Django 4.2.7 on 2023-11-20 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pharmacy', '0003_addmedicine_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_alter_customer_user_alter_pharmacist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.addmedicine')),
                ('pharmacist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacist_medicines', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
