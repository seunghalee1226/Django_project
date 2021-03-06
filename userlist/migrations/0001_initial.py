# Generated by Django 3.1.2 on 2020-12-01 00:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userlist',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('secret', models.UUIDField(default=uuid.uuid4)),
                ('is_active', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('modify_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
