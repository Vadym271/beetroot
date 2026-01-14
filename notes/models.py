from django.db import models


class Category(models.Model):
    title = models.CharField("Category's title")

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField('Title')
    text = models.TextField("Note's text")
    reminder = models.DateTimeField('remind me on')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/"