from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from elements.models import Task


class TaskOrderingTests(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(
            content="Task 1",
            is_done=False,
            created_at=timezone.now() - timedelta(days=1)
        )
        self.task2 = Task.objects.create(
            content="Task 2",
            is_done=True,
            created_at=timezone.now()
        )
        self.task3 = Task.objects.create(
            content="Task 3",
            is_done=False,
            created_at=timezone.now()
        )

    def test_task_ordering(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], self.task3)
        self.assertEqual(tasks[1], self.task1)
        self.assertEqual(tasks[2], self.task2)
