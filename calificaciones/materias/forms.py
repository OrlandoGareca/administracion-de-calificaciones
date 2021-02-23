from django import forms
from calificaciones.materias.models import Gestion
from django.contrib.admin import widgets 
class GestionForm(forms.ModelForm):    
    gestion = forms.DateField(label="Gestion", required=False,widget=widgets.AdminDateWidget)
    class Meta:
        model = Gestion
        fields = ("gestion",)
