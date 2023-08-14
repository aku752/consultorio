from django.urls import path
from .views import (index, perfil, table, paciente,
                    farmacia, tratamiento, prescripcion,
                    finanza, administracion, cita)

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('table/', table, name='table'),
    path('paciente/',paciente, name='paciente'),   
    path('farmacia/',farmacia, name='farmacia'),   
    path('tratamiento/',tratamiento, name='tratamiento'),   
    path('prescripcion/',prescripcion, name='prescripcion'),   
    path('finanza/',finanza, name='finanza'),   
    path('administracion/',administracion, name='administracion'),   
    path('cita/',cita, name='cita'),   
]
