# Generated by Django 4.0.6 on 2022-08-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0002_receipt_teacher_studentid_staff_schoolfees_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='unit_specialty',
            new_name='occupation_specialty',
        ),
        migrations.AlterField(
            model_name='school',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolaccount',
            name='account_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='emergency_contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]