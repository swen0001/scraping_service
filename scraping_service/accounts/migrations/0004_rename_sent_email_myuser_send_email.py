# Generated by Django 4.1 on 2022-08-16 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_myuser_groups_remove_myuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='sent_email',
            new_name='send_email',
        ),
    ]
