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
    

def coursesPage(request):
    '''Страница курсов'''
    courses = Course.objects.all()
    categories = Category.objects.all()
    age = Age.objects.all()

    context = {'courses': courses, 'categories': categories, 'age': age}

    return render(request=request, template_name='blablycode_app/courses.html', context=context)
