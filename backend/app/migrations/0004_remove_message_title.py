# Generated by Django 2.2.4 on 2019-09-14 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
    ]
