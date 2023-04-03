from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoList, name='todo-list'),
]
