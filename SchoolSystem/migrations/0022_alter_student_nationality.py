# Generated by Django 4.1 on 2022-09-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0021_alter_student_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('Rwanda', 'Rwanda'), ('Uganda', 'Uganda'), ('Kenya', 'Kenya'), ('South Sudan', 'South Sudan'), ('Tanzania', 'Tanzania')], max_length=30, null=True),
        ),
    ]
