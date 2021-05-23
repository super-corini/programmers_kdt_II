# Generated by Django 3.2.3 on 2021-05-18 14:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('is_limited_edition', models.BooleanField(default=False)),
                ('brand', models.CharField(choices=[('Nike', 'Nike'), ('Adidas', 'Adidas')], max_length=8)),
            ],
        ),
    ]
