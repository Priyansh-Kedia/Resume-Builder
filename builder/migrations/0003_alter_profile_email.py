# Generated by Django 4.0 on 2022-06-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]