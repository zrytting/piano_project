# Generated by Django 4.2 on 2024-03-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
