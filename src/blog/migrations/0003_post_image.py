# Generated by Django 2.2.10 on 2020-03-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_blog.png', height_field=400, max_length=200, upload_to='', width_field=600),
        ),
    ]
