# Generated by Django 3.2.3 on 2021-05-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_bugger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugger',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
