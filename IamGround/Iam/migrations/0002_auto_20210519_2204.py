# Generated by Django 3.2.3 on 2021-05-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='income_mean',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='document_deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
