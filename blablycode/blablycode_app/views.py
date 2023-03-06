from cProfile import Profile
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, TemplateView
from .forms import *
from django.contrib import messages
from  django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import *


class Index(CreateView):
    '''Главная страница'''
    template_name = 'blablycode_app/index.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

def courses_page(request):
    '''Страница курсов'''
    courses = Course.objects.all()
    categories = Category.objects.all()
    age = Age.objects.all()

    context = {'courses': courses, 'categories': categories, 'age': age}

    return render(request=request, template_name='blablycode_app/courses.html', context=context)


def get_courses_category(request, category_id):
    '''Страница для сортировки курсов по категориям'''
    courses = Course.objects.filter(course_category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    age = Age.objects.all()

    context = {'courses': courses, 'categories': categories, 'age': age, 'category': category}

    return render(request=request, template_name='blablycode_app/courses_category.html', context=context)


def get_courses_age(request, age_id):
    '''Страница для сортировки курсов по категориям'''
    courses = Course.objects.filter(course_age_id=age_id)
    categories = Category.objects.all()
    ages = Age.objects.all()
    age = Age.objects.get(pk=age_id)

    context = {'courses': courses, 'categories': categories, 'age': age, 'ages': ages}

    return render(request=request, template_name='blablycode_app/courses_age.html', context=context)