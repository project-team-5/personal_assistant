from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note-list'),
    path('create/', views.NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('<int:pk>/update/', views.NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),
    path('search/', views.NoteSearchView.as_view(), name='note-search'),
]

