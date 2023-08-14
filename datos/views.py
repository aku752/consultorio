from django.shortcuts import render
from .models import Paciente

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def perfil(request):
    return render(request, 'profile.html',{})

def table(request):
    return render(request, 'table.html', {})

def paciente(request):
    paciente = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes':paciente})

def farmacia(request):
    return render(request, 'farmacia.html')

def tratamiento(request):
    return render(request, 'tratamiento.html')

def prescripcion(request):
    return render(request, 'prescripcion.html')

def finanza(request):
    return render(request, 'finanza.html')

def administracion(request):
    return render(request, 'administracion.html')

def cita(request):
    return render(request, 'citas.html')