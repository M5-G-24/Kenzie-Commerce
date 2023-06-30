# Generated by Django 4.0.7 on 2023-06-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('disponibility', models.CharField(choices=[('AVALIABLE', 'Avaliable'), ('UNAVALIABLE', 'Unavaliable')], max_length=11)),
            ],
        ),
    ]
