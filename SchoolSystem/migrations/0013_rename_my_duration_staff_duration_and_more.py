# Generated by Django 4.1 on 2022-08-29 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0012_rename_period_staff_my_duration_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='My_Duration',
            new_name='Duration',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='My_gender',
            new_name='Mygender',
        ),
    ]
