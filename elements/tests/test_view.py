from django.test import TestCase, Client
from django.urls import reverse

from elements.models import Task, Tag


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task")
        self.task.tags.add(self.tag)

    def test_task_list_view(self):
        response = self.client.get(reverse("elements:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "elements/task_list.html")
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        task_data = {
            "content": "New Task",
            "tags": [self.tag.id]
        }
        response = self.client.post(
            reverse("elements:task-create"),
            task_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())

    def test_task_update_view(self):
        task_data = {
            "content": "Updated Task",
            "tags": [self.tag.id]
        }
        response = self.client.post(
            reverse("elements:task-update", args=[self.task.id]),
            task_data
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")

    def test_task_delete_view(self):
        response = self.client.post(
            reverse("elements:task-delete", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_task_update_status(self):
        self.assertFalse(self.task.is_done)
        response = self.client.get(
            reverse("elements:task-update-status", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

    def test_tag_list_view(self):
        response = self.client.get(reverse("elements:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "elements/tag_list.html")
        self.assertContains(response, "Test Tag")

    def test_tag_create_view(self):
        tag_data = {"name": "New Tag"}
        response = self.client.post(
            reverse("elements:tag-create"),
            tag_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

    def test_tag_update_view(self):
        tag_data = {"name": "Updated Tag"}
        response = self.client.post(
            reverse("elements:tag-update", args=[self.tag.id]),
            tag_data
        )
        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated Tag")

    def test_tag_delete_view(self):
        response = self.client.post(
            reverse("elements:tag-delete", args=[self.tag.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())
