from django import forms
from django.forms import ModelForm, TextInput

from encurtador.models import URLCurta

class URLCurtaForm(ModelForm):
    """
    Formulário para criação de uma URL curta
    """

    destino = forms.URLField(
        widget=TextInput(attrs={'placeholder': 'Insira a URL para encurtar'})
    )

    class Meta:
        model = URLCurta
        fields = ['destino']
