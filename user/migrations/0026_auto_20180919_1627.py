# Generated by Django 2.0.7 on 2018-09-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20180907_0653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='team_colloquiom',
            new_name='team_colloquium',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='team_this_way_or_that_way',
            new_name='team_this_way_that_way',
        ),
    ]
