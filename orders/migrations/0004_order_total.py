# Generated by Django 4.0.7 on 2023-07-06 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=99),
            preserve_default=False,
        ),
    ]
