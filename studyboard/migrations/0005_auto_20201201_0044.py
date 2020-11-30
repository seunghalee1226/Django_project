# Generated by Django 3.1.2 on 2020-12-01 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyboard', '0004_auto_20201130_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studyboard',
            options={'ordering': ('-modify_dt',), 'verbose_name': 'studyboard', 'verbose_name_plural': 'studyboards'},
        ),
        migrations.RemoveField(
            model_name='studyboard',
            name='description',
        ),
        migrations.AlterField(
            model_name='studyboard',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name='USER'),
        ),
    ]