# Generated by Django 2.0.7 on 2018-09-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_merge_20180902_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='event',
            field=models.CharField(default='Questionnaire', max_length=100),
            preserve_default=False,
        ),
    ]