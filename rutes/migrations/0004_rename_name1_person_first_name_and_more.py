# Generated by Django 5.1.1 on 2024-10-08 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutes', '0003_campus_interestpoint_person_trailtype_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name1',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name2',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name3',
            new_name='second_name',
        ),
    ]
