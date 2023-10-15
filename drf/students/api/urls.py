

from django.urls import path
from students.api.views import hello_world, index
urlpatterns = [
    path('hello', hello_world,name='api.hello_world'),
    path('', index, name='students.api.index')
]