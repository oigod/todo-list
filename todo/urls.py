from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='todo-list'),
    path('tags-list/', views.TagsListView.as_view(), name='tags-list'),
    path('<int:pk>/switch-todo-status/', views.switch_todo_status, name='switch-todo-status'),
]
