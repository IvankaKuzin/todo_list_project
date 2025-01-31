from django.contrib import admin

from elements.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
