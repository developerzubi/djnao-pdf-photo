# Generated by Django 4.2.12 on 2024-05-09 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_quiz_remove_assignmentinstructions_assessment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizquestion',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
    ]
