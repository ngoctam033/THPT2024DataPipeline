# Generated by Django 5.1 on 2024-08-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyzer_score', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimstudents',
            name='student_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
