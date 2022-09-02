# Generated by Django 4.1 on 2022-08-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0004_alter_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Prefer not to say', 'Prefer not to say')], max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stream',
            field=models.CharField(choices=[('Adalab', 'Adalab'), ('Annita B', 'Annita B'), ('Hopper Lab', 'Hopper Lab')], max_length=15, null=True),
        ),
    ]
