# Generated by Django 5.0.2 on 2024-02-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphones',
            name='memory',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='smartphones',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='smartphones',
            name='ram',
            field=models.IntegerField(),
        ),
    ]