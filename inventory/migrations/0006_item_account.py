# Generated by Django 2.2.9 on 2020-01-26 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20200126_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Account'),
        ),
    ]
