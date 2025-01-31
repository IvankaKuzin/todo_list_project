from django.urls import path

from elements.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    task_update_status
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/update-status/",
        task_update_status,
        name="task-update-status",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
    path("tag-create/", TagCreateView.as_view(), name="tag-create"),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
]

app_name = "elements"
