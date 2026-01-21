from .forms import NoteForm
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
import adispatch
from asgiref.sync import sync_to_async
from django.views import View


async def index(request):
    is_auth = await sync_to_async(lambda: request.user.is_authenticated)()

    if not is_auth:
        return redirect('login')

    user = await sync_to_async(lambda: request.user)()
    notes = [note async for note in Note.objects.filter(author=user)]
    return render(request, "notes/my_notes.html", {'notes': notes})


async def create_note(request):
    if not request.user.is_authenticated:
        return redirect('login')

    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            def save_note():
                note = form.save(commit=False)
                note.author = request.user
                note.save()
                return note

            await sync_to_async(save_note)()
            return redirect('index')
        else:
            error = 'Form is incorrectly filled'
    else:
        form = NoteForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'notes/create.html', data)


class NoteUpdate(View):
    async def get(self, request, pk):
        user = await request.auser()
        if not user.is_authenticated:
            return redirect('login')

        try:
            note = await Note.objects.filter(author=user).aget(pk=pk)
        except Note.DoesNotExist:
            return redirect('index')

        form = NoteForm(instance=note)

        async_render = sync_to_async(render)
        return await async_render(request, 'notes/create.html', {'form': form})

    async def post(self, request, pk):
        user = await request.auser()
        try:
            note = await Note.objects.filter(author=user).aget(pk=pk)
        except Note.DoesNotExist:
            return redirect('index')

        form = NoteForm(request.POST, instance=note)

        if await sync_to_async(form.is_valid)():
            await sync_to_async(form.save)()
            return redirect('index')

        async_render = sync_to_async(render)
        return await async_render(request, 'notes/create.html', {'form': form})

class NoteDelete(View):
    async def get(self, request, pk):
        user = await request.auser()
        if not user.is_authenticated:
            return redirect('login')

        try:
            note = await Note.objects.filter(author=user).aget(pk=pk)
        except Note.DoesNotExist:
            return redirect('index')

        async_render = sync_to_async(render)
        return await async_render(request, 'notes/delete.html', {'note': note})

    async def post(self, request, pk):
        user = await request.auser()
        try:
            note = await Note.objects.filter(author=user).aget(pk=pk)
            await note.adelete()
        except Note.DoesNotExist:
            pass

        return redirect('index')