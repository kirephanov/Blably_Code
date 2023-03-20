from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('courses/', courses_page, name='courses'),
    path('courses/category/<int:category_id>/', get_courses_category, name='courses_category'),
    path('courses/age/<int:age_id>/', get_courses_age, name='courses_age'),
    path('course/<int:course_id>/', open_course_page, name='open_course'),
    path('news/<int:pk>/', GetLesson.as_view(), name='lesson'),
    path('homework/', homework_page, name='homework'),
    path('compiler/', Compiler.as_view(), name='compiler'),
    path('practice/', PracticeMenu.as_view(), name='practice_menu'),
    path('practice/exercise/', exercises_page, name='exercise'),
]