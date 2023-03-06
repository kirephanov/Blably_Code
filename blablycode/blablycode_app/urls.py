from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('courses/', courses_page, name='courses'),
    path('courses/category/<int:category_id>/', get_courses_category, name='courses_category'),
]