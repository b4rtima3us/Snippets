from django.forms import ModelForm, Textarea, TextInput, CheckboxInput
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'public', 'code']
        labels = {'name': '', 'lang': '', 'public': '', 'code': ''}
        widgets = {
            'name': TextInput(attrs={
                "class": "form-control", 'style': 'max-width: 350px', 'placeholder': 'Название сниппета'
            }),
            'public': CheckboxInput(attrs={'id': 'public'}),
            'code': Textarea(attrs={
                "class": "form-control", 'style': 'max-width: 350px', 'placeholder': 'Код сниппета'
            })
        }
