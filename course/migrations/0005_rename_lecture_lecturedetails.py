# Generated by Django 4.1.1 on 2022-09-18 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_lecture_c_id_lecture_coursedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='lecture',
            new_name='lecturedetails',
        ),
    ]
