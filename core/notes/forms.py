from django import forms
from .models import Note, Tag

class NoteForm(forms.ModelForm):
    new_tags = forms.CharField(max_length=255, required=False, help_text='Введіть нові теги через кому')

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super(NoteForm, self).save(commit=False)
        new_tags = self.cleaned_data.get('new_tags', '')
        if commit:
            instance.save()
            if new_tags:
                tag_names = [name.strip() for name in new_tags.split(',')]
                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    instance.tags.add(tag)
        return instance
    
    