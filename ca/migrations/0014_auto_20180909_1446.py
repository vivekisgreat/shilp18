# Generated by Django 2.0.5 on 2018-09-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0013_auto_20180717_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
