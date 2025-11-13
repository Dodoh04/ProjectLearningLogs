from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']  # ou o nome correto do campo no modelo
        labels = {'text': 'Tópico'}
