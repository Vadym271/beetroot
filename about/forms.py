from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'article name'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'preview'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'article content'
            }),
        }

