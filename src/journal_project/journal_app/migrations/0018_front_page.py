# Generated by Django 3.2.7 on 2021-11-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0017_alter_uploads_manuscriptword'),
    ]

    operations = [
        migrations.CreateModel(
            name='front_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider1', models.FileField(upload_to='frontpage/')),
                ('logo', models.FileField(upload_to='frontpage/')),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('logo_text', models.TextField(max_length=100)),
            ],
        ),
    ]