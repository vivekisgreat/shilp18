# Generated by Django 2.0.7 on 2018-09-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0007_quiz_team_allanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_team',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
