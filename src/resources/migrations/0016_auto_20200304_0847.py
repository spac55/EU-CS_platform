# Generated by Django 2.2.10 on 2020-03-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0015_auto_20200304_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='theme',
        ),
        migrations.AddField(
            model_name='resource',
            name='theme',
            field=models.ManyToManyField(to='resources.Theme'),
        ),
    ]
