from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Tag
from .forms import NoteForm


# Клас для відображення списку нотаток
class NoteListView(ListView):
    model = Note  
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'


# Клас для відображення деталей окремої нотатки
class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'


# Клас для створення нової нотатки
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note-list')

    def form_valid(self, form):
        response = super().form_valid(form)  # Зберігаємо форму і отримуємо відповідь
        new_tags = self.request.POST.get('new_tags')  # Отримуємо нові теги з POST-запиту
        if new_tags:
            tags = [tag.strip() for tag in new_tags.split(',')]  # Розділяємо і очищуємо теги
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(name=tag)  # Перевіряємо і створюємо теги
                self.object.tags.add(tag_obj)  # Додаємо теги до нотатки
        return response  # Повертаємо відповідь


# Клас для оновлення існуючої нотатки
class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        new_tags = self.request.POST.get('new_tags')
        if new_tags:
            tags = [tag.strip() for tag in new_tags.split(',')]
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                self.object.tags.add(tag_obj)
        return response


# Клас для видалення нотатки
class NoteDeleteView(DeleteView):
    model = Note  
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note-list')


# Клас для пошуку нотаток
class NoteSearchView(ListView):
    model = Note  
    template_name = 'notes/note_search.html'
    context_object_name = 'notes'

    def get_queryset(self):
        query = self.request.GET.get('q')  
        return Note.objects.filter(
            title__icontains=query) | Note.objects.filter(
            content__icontains=query) | Note.objects.filter(
            tags__name__icontains=query).distinct()  # Пошук нотаток за заголовком, вмістом і тегами