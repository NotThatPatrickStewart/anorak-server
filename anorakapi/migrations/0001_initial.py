# Generated by Django 3.1.7 on 2021-03-24 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Whiskey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('list_img_url', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WhiskeyTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normalized_count', models.IntegerField()),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatedtag', to='anorakapi.tag')),
                ('whiskey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatedwhiskey', to='anorakapi.whiskey')),
            ],
        ),
        migrations.CreateModel(
            name='UserWhiskey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('list_img_url', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=500)),
                ('rating', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('whiskey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anorakapi.whiskey')),
            ],
        ),
    ]
