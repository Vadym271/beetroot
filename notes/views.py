from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, "notes/my_notes.html", {'notes': notes})
@login_required
def create_note(request):
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
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
    form_class = NoteForm

class NoteDelete(DeleteView):
    model = Note
    template_name = 'notes/delete.html'
    success_url = '/'