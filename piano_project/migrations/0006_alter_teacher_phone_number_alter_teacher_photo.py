# Generated by Django 5.0.4 on 2024-04-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano_project', '0005_alter_teacher_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
