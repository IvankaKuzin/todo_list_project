from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from elements.models import Task, Tag
from elements.forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "elements/task_list.html"
    context_object_name = "task_list"


class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("elements:task-list")
    form_class = TaskForm


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("elements:task-list")
    form_class = TaskForm


def task_update_status(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()

    return redirect(reverse("elements:task-list"))


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("elements:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "elements/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("elements:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("elements:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("elements:tag-list")
