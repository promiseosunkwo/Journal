# Generated by Django 3.2.6 on 2021-09-25 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal_app', '0013_alter_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Uzer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='journal_app.uzer'),
        ),
    ]