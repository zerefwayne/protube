# Generated by Django 3.0.3 on 2020-02-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt_search', '0004_auto_20200211_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubevideo',
            name='id',
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='videoId',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]
