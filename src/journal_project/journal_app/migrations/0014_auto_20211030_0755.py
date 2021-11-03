# Generated by Django 3.2.7 on 2021-10-30 06:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0013_publish_published_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='date_published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='publish',
            name='rand',
            field=models.BooleanField(default=False),
        ),
    ]