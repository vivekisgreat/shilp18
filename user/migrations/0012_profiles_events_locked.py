# Generated by Django 2.1 on 2018-09-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20180902_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='events_locked',
            field=models.BooleanField(default=False),
        ),
    ]
