# Generated by Django 4.1 on 2022-08-29 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0009_rename_occupation_specialty_staff_specialty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='Specialty',
            new_name='occupation_specialty',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='period',
            new_name='work_period',
        ),
    ]
