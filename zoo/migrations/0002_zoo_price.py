# Generated by Django 4.2.7 on 2023-12-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoo',
            name='price',
            field=models.DecimalField(decimal_places=2, default=9.99, max_digits=6),
        ),
    ]