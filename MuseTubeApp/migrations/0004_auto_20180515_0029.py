# Generated by Django 2.0.5 on 2018-05-15 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MuseTubeApp', '0003_auto_20180514_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='title',
        ),
    ]
