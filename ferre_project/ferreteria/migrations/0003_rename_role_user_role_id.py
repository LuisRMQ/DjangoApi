# Generated by Django 5.0.6 on 2024-06-10 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0002_remove_user_name_role_description_user_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='role_id',
        ),
    ]
