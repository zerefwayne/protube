# Generated by Django 3.0.3 on 2020-02-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('videoId', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('publishedAt', models.DateTimeField()),
                ('videoTitle', models.CharField(max_length=500)),
                ('thumbnailUrl', models.CharField(max_length=500)),
                ('channelTitle', models.CharField(max_length=500)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
