# Generated by Django 2.2 on 2021-04-15 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name_here', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='User',
        ),
    ]