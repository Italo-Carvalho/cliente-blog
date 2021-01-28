# Generated by Django 3.1.5 on 2021-01-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_facebook_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='twitter_link',
            field=models.URLField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='facebook_link',
            field=models.URLField(blank=True, editable=False),
        ),
    ]
