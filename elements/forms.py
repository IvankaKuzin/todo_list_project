from django.forms import (
    ModelForm,
    ModelMultipleChoiceField,
    CheckboxSelectMultiple
)
from django.forms.fields import DateTimeField

from elements.models import Tag, Task


class TaskForm(ModelForm):
    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
