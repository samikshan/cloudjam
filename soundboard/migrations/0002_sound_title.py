# Generated by Django 2.0.4 on 2018-04-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='title',
            field=models.CharField(default='DazedNConfused', help_text='Enter title for music piece', max_length=500, unique=True),
        ),
    ]