from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.views.generic import UpdateView, DeleteView

# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request, "notes/my_notes.html", {'notes': notes})

def create_note(request):
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Form is incorrectly filled'
    form = NoteForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'notes/create.html', data)

class NoteUpdate(UpdateView):
    model = Note
    template_name = 'notes/create.html'
    fields = ['title', 'text', 'reminder', 'category']

class NoteDelete(DeleteView):
    model = Note
    template_name = 'notes/delete.html'
    success_url = '/'