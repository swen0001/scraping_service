# Generated by Django 4.1 on 2022-08-09 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_language_alter_city_name_alter_city_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='name_c',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='name',
            new_name='name_l',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='slug',
            new_name='slug_l',
        ),
    ]