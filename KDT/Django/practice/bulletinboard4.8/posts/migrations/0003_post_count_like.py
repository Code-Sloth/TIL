# Generated by Django 3.2.18 on 2023-04-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230408_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count_like',
            field=models.IntegerField(default=0),
        ),
    ]
