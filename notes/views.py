from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request, "notes/my_notes.html", {'notes': notes})