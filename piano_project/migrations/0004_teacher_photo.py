# Generated by Django 5.0.4 on 2024-04-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano_project', '0003_teacher_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
