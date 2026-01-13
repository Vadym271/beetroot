from django.shortcuts import render, redirect
from .models import  Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

#from django.http import HttpResponse

# Create your views here.
def about_us(request):
    news = Article.objects.all()
    return render(request, 'about/about_us.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_us')
        else:
            error = 'Form was completed incorrectly'
    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'about/create.html', data)

class NewsDetailView(DetailView):
    model = Article
    template_name = 'about/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'about/create.html'

    fields = ['title', 'anons', 'full_text', 'date']


class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'about/news-delete.html'

    success_url = '/about/'
