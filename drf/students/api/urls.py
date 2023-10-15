

from django.urls import path
from students.api.views import hello_world
urlpatterns = [
    path('hello', hello_world,name='api.hello_world')
]