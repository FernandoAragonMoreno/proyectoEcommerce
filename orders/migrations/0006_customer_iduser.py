# Generated by Django 4.2.1 on 2023-06-14 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_city_idcountry'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='idUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.country'),
        ),
    ]
