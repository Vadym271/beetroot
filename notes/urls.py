from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_note', views.create_note, name='create_note'),
    path('<int:pk>/update', views.NoteUpdate.as_view(), name='update'),
    path('<int:pk>/delete', views.NoteDelete.as_view(), name='delete')
]