# Generated by Django 3.1.4 on 2020-12-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
