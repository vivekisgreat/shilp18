# Generated by Django 2.1 on 2018-09-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_team_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='payment_plan',
            field=models.IntegerField(default=0),
        ),
    ]