# Generated by Django 4.0 on 2021-12-11 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temparature', models.DecimalField(decimal_places=2, max_digits=12)),
                ('humidity', models.IntegerField()),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=12)),
                ('clouds', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
            ],
        ),
    ]
