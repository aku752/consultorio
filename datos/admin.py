from django.contrib import admin
from .models import Paciente

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display=('nombre','materno','paterno','estado')
    list_editable=('estado',)

admin.site.register(Paciente, PacienteAdmin)
