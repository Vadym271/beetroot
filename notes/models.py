from django.db import models
from django.conf import settings

class Category(models.Model):
    title = models.CharField("Category's title")

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField('Title')
    text = models.TextField("Note's text")
    reminder = models.DateTimeField('remind me on')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/"