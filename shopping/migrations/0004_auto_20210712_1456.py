# Generated by Django 3.2.4 on 2021-07-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default='', max_length=6),
        ),
    ]
