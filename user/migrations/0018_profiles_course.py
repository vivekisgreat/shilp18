# Generated by Django 2.0.7 on 2018-09-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20180904_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='course',
            field=models.CharField(default='Btech', max_length=100),
            preserve_default=False,
        ),
    ]
