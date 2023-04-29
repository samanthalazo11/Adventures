# Generated by Django 4.1.7 on 2023-04-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_restauraunts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excursions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
