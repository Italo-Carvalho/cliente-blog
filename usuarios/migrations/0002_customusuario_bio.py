# Generated by Django 3.1.5 on 2021-02-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusuario',
            name='bio',
            field=models.CharField(blank=True, max_length=100, verbose_name='bio'),
        ),
    ]
