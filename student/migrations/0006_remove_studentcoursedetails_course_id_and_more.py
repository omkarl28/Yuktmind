# Generated by Django 4.1.1 on 2022-09-18 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_course_coursedetails'),
        ('student', '0005_remove_studentcoursedetails_course_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcoursedetails',
            name='course_id',
        ),
        migrations.AddField(
            model_name='studentcoursedetails',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.coursedetails'),
        ),
    ]
