# Generated by Django 5.0.2 on 2024-03-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_smartphones_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphones',
            name='release_date',
            field=models.DateField(),
        ),
    ]
