# Generated by Django 4.1.1 on 2022-10-04 21:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coffeehouse', '0003_rename_bike_frendly_coffeehouse_bike_friendly'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('house', models.ManyToManyField(to='coffeehouse.coffeehouse')),
                ('name', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
