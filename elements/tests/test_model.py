from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from elements.models import Task, Tag


class ModelTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            content="Test Task",
            deadline=timezone.now() + timedelta(days=1)
        )
        self.task.tags.add(self.tag)

    def test_tag_str_method(self):
        self.assertEqual(str(self.tag), "Test Tag")

    def test_task_str_method(self):
        expected = (f"{self.task.content} "
                    f"({self.task.is_done}) "
                    f"[{self.task.tags}]")
        self.assertEqual(str(self.task), expected)

    def test_task_creation(self):
        self.assertFalse(self.task.is_done)
        self.assertEqual(self.task.content, "Test Task")
        self.assertTrue(self.task.deadline > timezone.now())
        self.assertEqual(self.task.tags.count(), 1)
        self.assertEqual(self.task.tags.first(), self.tag)
