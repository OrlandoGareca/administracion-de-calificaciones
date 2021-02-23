from django.contrib import admin
from calificaciones.materias.models import Materias,Grado,Turno,Aulas,Gestion
from calificaciones.materias.forms import GestionForm
# Register your models here.
admin.site.register(Materias)
admin.site.register(Grado)
admin.site.register(Turno)
admin.site.register(Aulas)


class GestionAdmin(admin.ModelAdmin):
    form = GestionForm
    list_display = ( "gestion", "only_year")
admin.site.register(Gestion)
