# Generated by Django 5.1 on 2024-08-11 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Analyzer_score', '0009_rename_student_factscores_student_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factscores',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='factscores',
            old_name='subject_id',
            new_name='subject',
        ),
    ]
