# Generated by Django 4.1 on 2022-08-09 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_rename_slug_city_slug_c'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name_c',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='slug_c',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='name_l',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='slug_l',
            new_name='slug',
        ),
    ]