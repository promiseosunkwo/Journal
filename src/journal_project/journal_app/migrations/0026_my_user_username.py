# Generated by Django 3.2.6 on 2021-09-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0025_my_user_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='username',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
