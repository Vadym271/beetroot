from django.db import models

class Article(models.Model):
    title = models.CharField('Name', max_length=50, default='Anonimus')
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('publication date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/about/{self.id}'
