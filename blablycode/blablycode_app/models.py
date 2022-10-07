from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Course(models.Model):
    '''Класс отображает курсы для обучающихся'''
    сourse_title = models.CharField(max_length=150, verbose_name='Название курса')
    course_icon = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Иконка курса', blank=True)
    course_description = models.TextField(max_length=250, verbose_name='Описание курса')
    course_category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    course_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.сourse_title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-course_created_at']


class Lesson(models.Model):
    '''Класс отображает видеоуроки для обучающихся'''
    lesson_title = models.CharField(max_length=150, verbose_name='Название курса')
    lesson_сourse = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name='Курс')
    lesson_video = models.CharField(max_length=150, verbose_name='Видео') # Ссылка на видео
    lesson_description = models.TextField(max_length=150, verbose_name='Описание урока')
    lesson_exercise = models.TextField(max_length=500, verbose_name='Задание урока')
    lesson_homework = models.TextField(max_length=500, verbose_name='Домашнее задание')
    lesson_code_editor = models.CharField(max_length=150, verbose_name='Редактор кода')
    lesson_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.lesson_title

    class Meta:
        verbose_name = 'Видеоурок'
        verbose_name_plural = 'Видеоуроки'
        ordering = ['-lesson_created_at']


class Category(models.Model):
    '''Класс отображает категории для курсов и уроков'''
    category_title = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_title']


def user_directory_path(instance, filename):
    # Файл будет загружен в MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Homework(models.Model):
    '''Класс отображает домашние задания обучающийся'''
    homework_title = models.CharField(max_length=50, default='Домашнее задание', blank=True, verbose_name='Домашнее задание') # Используется в __str__
    homework_course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name='Курс')
    homework_lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT, null=True, verbose_name='Урок')
    homework_author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Выполнил')
    homework_file = models.FileField(upload_to=user_directory_path, verbose_name='Файл')
    homework_verified = models.BooleanField(blank=True, verbose_name='Проверено')
    homework_comment = models.CharField(max_length=250, verbose_name='Комментарий к заданию') 


    def __str__(self):
        return self.homework_title

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


