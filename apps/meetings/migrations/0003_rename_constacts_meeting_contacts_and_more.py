# Generated by Django 4.1.2 on 2023-02-01 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_rename_meetings_meeting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='constacts',
            new_name='contacts',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='data',
            new_name='date',
        ),
    ]
