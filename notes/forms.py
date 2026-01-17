from .models import Note
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']

        widgets = {
          "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'note name'
          }),
          "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'note text'
          }),
          "reminder": DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'remind me on'
          }),

        }
