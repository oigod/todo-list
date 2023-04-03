from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from . import models


class ToDoListView(generic.ListView):
    model = models.Task
    context_object_name = 'todo_list'
    template_name = 'todo_templates/todo_list.html'
    paginate_by = 5


def switch_todo_status(request, pk: int):
    task = get_object_or_404(models.Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:todo-list")
