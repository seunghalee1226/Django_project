# Generated by Django 3.1.2 on 2020-11-30 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
