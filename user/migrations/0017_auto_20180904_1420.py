# Generated by Django 2.0.7 on 2018-09-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20180903_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='residential_address',
            new_name='ca_name',
        ),
        migrations.AddField(
            model_name='profiles',
            name='money',
            field=models.CharField(default='300', max_length=100),
            preserve_default=False,
        ),
    ]
