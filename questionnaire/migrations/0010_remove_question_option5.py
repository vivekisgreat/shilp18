# Generated by Django 2.0.7 on 2018-09-22 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_auto_20180922_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option5',
        ),
    ]