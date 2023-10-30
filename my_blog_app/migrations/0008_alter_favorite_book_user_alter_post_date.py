# Generated by Django 4.2.2 on 2023-10-29 15:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_blog_app', '0007_favorite_book_delete_favorite_remove_post_follows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite_book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 16, 41, 24, 116777), verbose_name='Date Published'),
        ),
    ]
