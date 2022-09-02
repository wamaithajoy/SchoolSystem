# Generated by Django 4.1 on 2022-08-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0017_alter_student_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('Rwanda', 'Rwanda'), ('Tanzania', 'Tanzania'), ('Kenya', 'Kenya'), ('Uganda', 'Uganda'), ('South Sudan', 'South Sudan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='unit_specialty',
            field=models.CharField(choices=[('Python', 'Python'), ('Kotlin', 'Kotlin'), ('FR', 'Frontendweb'), ('IOT', 'IOT'), ('Research', 'UserResearch'), ('Design', 'UI/UX Design'), ('PD', 'Professiondevelopment'), ('NYJ', 'Navigating Your Journey')], max_length=11, null=True),
        ),
    ]
