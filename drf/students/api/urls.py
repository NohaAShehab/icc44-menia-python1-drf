

from django.urls import path
from students.api.views import hello_world, index, student_resource
urlpatterns = [
    path('hello', hello_world,name='api.hello_world'),
    path('', index, name='students.api.index'),
    path('<int:id>',student_resource, name='students.api.resource')
]