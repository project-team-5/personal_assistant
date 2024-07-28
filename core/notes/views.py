from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Tag

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    template_name = 'notes/note_detail.html'  

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')
    
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')

class NoteSearchView(ListView):
    model = Note
    template_name = 'notes/note_search.html'
    context_object_name = 'notes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Note.objects.filter(title__icontains=query) | Note.objects.filter(content__icontains=query)
    

