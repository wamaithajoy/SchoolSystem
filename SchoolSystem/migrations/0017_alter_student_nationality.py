# Generated by Django 4.1 on 2022-08-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0016_rename_phone_number_student_my_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('Kenya', 'Kenya'), ('Rwanda', 'Rwanda'), ('Tanzania', 'Tanzania'), ('South Sudan', 'South Sudan'), ('Uganda', 'Uganda')], max_length=30, null=True),
        ),
    ]
