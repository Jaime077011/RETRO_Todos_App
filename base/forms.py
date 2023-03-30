from django import forms
from .models import Task, User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'nes-input'}),
            'description': forms.Textarea(attrs={'class': 'nes-textarea'}),
        }

