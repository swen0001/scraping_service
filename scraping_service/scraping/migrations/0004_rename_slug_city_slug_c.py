# Generated by Django 4.1 on 2022-08-09 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_rename_name_city_name_c_rename_name_language_name_l_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='slug',
            new_name='slug_c',
        ),
    ]