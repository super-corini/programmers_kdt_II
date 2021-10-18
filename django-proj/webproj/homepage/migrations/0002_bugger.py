# Generated by Django 3.2.3 on 2021-05-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bugger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('is_set', models.BooleanField(default=False)),
            ],
        ),
    ]
