# Generated by Django 3.1.2 on 2020-11-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('description', models.CharField(blank=True, help_text='simple description text.', max_length=100, verbose_name='DESCRIPTION')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='TITLE')),
            ],
            options={
                'verbose_name': 'notice',
                'verbose_name_plural': 'notices',
                'db_table': 'notice_posts',
                'ordering': ('-modify_dt',),
            },
        ),
    ]
