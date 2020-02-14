from django import forms
from django.forms import ModelForm

from encurtador.models import Encurtador

class EncutadorForm(ModelForm):
    url_curta = forms.CharField(required=False)
    class Meta:
        model = Encurtador
        fields = ['destino']