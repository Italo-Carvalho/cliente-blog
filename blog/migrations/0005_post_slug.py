# Generated by Django 3.1.5 on 2021-01-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug'),
        ),
    ]
