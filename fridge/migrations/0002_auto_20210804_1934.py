# Generated by Django 3.2.5 on 2021-08-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.AddField(
            model_name='dish',
            name='add',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='dish',
            name='main',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dish',
            name='option',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='intro',
            field=models.TextField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
    ]
