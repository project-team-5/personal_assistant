from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Tag
from django.contrib.auth.mixins import LoginRequiredMixin

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    # template_name = 'notes/note_detail.html'  


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note_list')


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note_list')


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note_list')


class NoteSearchView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_search.html'
    context_object_name = 'notes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Note.objects.filter(title__icontains=query) | Note.objects.filter(content__icontains=query)
    

