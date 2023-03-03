# Generated by Django 3.2.5 on 2023-03-03 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blablycode_app', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_name', models.CharField(max_length=150, verbose_name='Имя пользователя')),
                ('feedback_email', models.CharField(max_length=150, verbose_name='Почта')),
                ('feedback_message', models.TextField(max_length=500, verbose_name='Сообщение')),
                ('feedback_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
                'ordering': ['-feedback_created_at'],
            },
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_title',
            field=models.CharField(max_length=150, verbose_name='Название урока'),
        ),
        migrations.CreateModel(
            name='TechTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_task_title', models.CharField(max_length=150, verbose_name='Название ТЗ')),
                ('tech_task_content', models.TextField(max_length=1500, verbose_name='Содержание ТЗ')),
                ('tech_task_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blablycode_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Техническое задание',
                'verbose_name_plural': 'Технические задания',
            },
        ),
        migrations.CreateModel(
            name='InterviewExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_title', models.CharField(max_length=150, verbose_name='Название задачи')),
                ('interview_content', models.TextField(max_length=500, verbose_name='Условие задачи')),
                ('interview_solve', models.TextField(max_length=500, verbose_name='Решение задачи')),
                ('interview_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blablycode_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Задача для собеседования',
                'verbose_name_plural': 'Задачи для собеседований',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_title', models.CharField(max_length=150, verbose_name='Название задачи')),
                ('exercise_content', models.TextField(max_length=500, verbose_name='Условие задачи')),
                ('exercise_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blablycode_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Задача для практики',
                'verbose_name_plural': 'Задачи для практики',
            },
        ),
    ]
