# Generated by Django 3.2.5 on 2021-07-13 14:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_alter_userdetails_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userdetails',
            new_name='UserDetail',
        ),
    ]