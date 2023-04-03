from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from . import models, forms


class ToDoListView(generic.ListView):
    model = models.Task
    context_object_name = 'todo_list'
    template_name = 'todo_templates/todo_list.html'
    paginate_by = 5


class ToDoTaskCreateView(generic.CreateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'todo_templates/task_form.html'
    success_url = reverse_lazy("todo:todo-list")


class ToDoTaskUpdateView(generic.UpdateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'todo_templates/task_form.html'
    success_url = reverse_lazy("todo:todo-list")


class ToDoTaskDeleteView(generic.DeleteView):
    model = models.Task
    template_name = 'todo_templates/task_confirm_delete.html'
    success_url = reverse_lazy("todo:todo-list")


class TagsListView(generic.ListView):
    model = models.Tag
    context_object_name = 'tags_list'
    template_name = 'todo_templates/tags_list.html'
    paginate_by = 5


def switch_todo_status(request, pk: int):
    task = get_object_or_404(models.Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:todo-list")
