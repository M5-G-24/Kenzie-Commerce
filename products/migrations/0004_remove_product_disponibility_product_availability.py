# Generated by Django 4.0.7 on 2023-07-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_user_alter_product_disponibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='disponibility',
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
