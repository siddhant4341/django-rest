# Generated by Django 5.1.3 on 2024-12-25 13:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('3e23cb45-54c4-46bf-be86-9d0bfdab21a7'), editable=False, primary_key=True, serialize=False),
        ),
    ]
