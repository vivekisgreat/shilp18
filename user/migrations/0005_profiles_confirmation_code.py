# Generated by Django 2.0.7 on 2018-09-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180901_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='confirmation_code',
            field=models.CharField(default='aajchajhs', max_length=100),
            preserve_default=False,
        ),
    ]
