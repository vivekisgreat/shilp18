# Generated by Django 2.0.7 on 2018-09-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180901_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='payment_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profiles',
            name='txid_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
