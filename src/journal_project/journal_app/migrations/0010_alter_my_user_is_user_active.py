# Generated by Django 3.2.7 on 2021-10-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0009_my_user_is_user_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='is_user_active',
            field=models.BooleanField(default=False),
        ),
    ]
