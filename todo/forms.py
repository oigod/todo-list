from django import forms

from . import models


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=models.Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
