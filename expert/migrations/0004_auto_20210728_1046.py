# Generated by Django 3.2.3 on 2021-07-28 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0003_auto_20210728_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='expert',
            name='user',
        ),
    ]
