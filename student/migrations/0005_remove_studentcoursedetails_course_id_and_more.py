# Generated by Django 4.1.1 on 2022-09-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_course_coursedetails'),
        ('student', '0004_alter_studentcoursedetails_course_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcoursedetails',
            name='course_id',
        ),
        migrations.AddField(
            model_name='studentcoursedetails',
            name='course_id',
            field=models.ManyToManyField(to='course.coursedetails'),
        ),
    ]
