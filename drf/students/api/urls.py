

from django.urls import path
from students.api.views import hello_world, index, student_resource

from students.api.student_views import  student_list
urlpatterns = [
    path('hello', hello_world,name='api.hello_world'),
    path('', index, name='students.api.index'),
    path('<int:id>',student_resource, name='students.api.resource'),
    path('models/', student_list, name='students.models.list')
]