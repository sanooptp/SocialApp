# Generated by Django 3.2.5 on 2021-07-14 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]