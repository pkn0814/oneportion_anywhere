# Generated by Django 3.2.3 on 2021-07-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0006_expert_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='photo',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
