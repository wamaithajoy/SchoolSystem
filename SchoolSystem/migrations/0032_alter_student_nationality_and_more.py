# Generated by Django 4.0.6 on 2022-10-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0031_student_profile_picture_alter_student_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('Rwanda', 'Rwanda'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda'), ('South Sudan', 'South Sudan'), ('Kenya', 'Kenya')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_picture/'),
        ),
    ]