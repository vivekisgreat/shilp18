# Generated by Django 2.0.5 on 2018-07-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0006_auto_20180709_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
