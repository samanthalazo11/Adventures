# Generated by Django 4.1.7 on 2023-04-29 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restauraunts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.destination')),
            ],
        ),
    ]
