# Generated by Django 2.1 on 2018-09-15 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20180903_0805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detail',
            options={'ordering': ('event', 'rank')},
        ),
    ]
