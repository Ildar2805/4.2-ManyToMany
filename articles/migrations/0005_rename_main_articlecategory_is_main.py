# Generated by Django 4.1 on 2022-08-10 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articlecategory_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlecategory',
            old_name='main',
            new_name='is_main',
        ),
    ]