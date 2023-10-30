# Generated by Django 4.2.2 on 2023-10-29 16:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_blog_app', '0012_alter_favorite_book_name_alter_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite_book',
            old_name='name',
            new_name='name_of_book',
        ),
        migrations.AlterField(
            model_name='favorite_book',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 17, 40, 5, 759442), verbose_name='Date Published'),
        ),
    ]
