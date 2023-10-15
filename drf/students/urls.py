
from django.urls import path
from students.views import  hello, acceptdata, students_index
urlpatterns = [

    path("hello", hello, name='students.hello'),
    path("accept", acceptdata, name='students.accept'),
    path('index',students_index, name= 'students.index' )
]