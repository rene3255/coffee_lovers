# Generated by Django 4.1.1 on 2022-10-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('wifi', models.BooleanField(default=True)),
                ('open_area', models.BooleanField(default=False)),
                ('silence_area', models.BooleanField(default=False)),
                ('vegan', models.BooleanField(default=False)),
                ('celiac', models.BooleanField(default=False)),
                ('bike_frendly', models.BooleanField(default=False)),
                ('price_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('toasters', models.BooleanField(default=False)),
                ('origen', models.CharField(blank=True, max_length=255, null=True)),
                ('machine', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
            },
        ),
    ]
