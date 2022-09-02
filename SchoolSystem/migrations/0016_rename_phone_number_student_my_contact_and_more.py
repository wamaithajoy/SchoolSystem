# Generated by Django 4.1 on 2022-08-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0015_rename_address_student_my_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone_number',
            new_name='my_contact',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='my_address',
        ),
        migrations.AddField(
            model_name='student',
            name='myaddress',
            field=models.CharField(max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('Uganda', 'Uganda'), ('South Sudan', 'South Sudan'), ('Tanzania', 'Tanzania'), ('Rwanda', 'Rwanda'), ('Kenya', 'Kenya')], max_length=30, null=True),
        ),
    ]