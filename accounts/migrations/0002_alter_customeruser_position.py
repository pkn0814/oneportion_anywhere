# Generated by Django 3.2.3 on 2021-07-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='position',
            field=models.CharField(choices=[('일반 사용자', '일반 사용자'), ('사업자', '사업자')], max_length=6, verbose_name='등급'),
        ),
    ]
