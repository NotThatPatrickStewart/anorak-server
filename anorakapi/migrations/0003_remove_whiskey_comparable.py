# Generated by Django 3.1.7 on 2021-03-17 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anorakapi', '0002_auto_20210315_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whiskey',
            name='comparable',
        ),
    ]
