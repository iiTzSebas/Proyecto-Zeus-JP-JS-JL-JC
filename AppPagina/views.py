from django.http import HttpResponse

from django.shortcuts import render

from.models import estudiante

from.forms import estudianteForm


# Create your views here.
def saludo(request):
    return HttpResponse("Buenas tardes a TODOS---")

def despedir(request):
    return HttpResponse("Hasta la vista Babys---")

def nosotros(request):
    return render(request, "nosotros.html")

def inicio(request):
    return render(request, "inicio.html")

def servicios(request):
    return render(request, "servicios.html")

def contacto(request):
    return render(request, "contacto.html")

def estudiantes(request):
    estudiantes = estudiante.objects.all()
    data = {
        
        'estudiantes':estudiantes
        }
    return render(request, "estudiantes/index.html", data) 

def crear(request):
    formulario = estudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
    return render(request, "estudiantes/crear.html", {'formulario':formulario }) 

def editar(request):
    return render(request, "estudiantes/editar.html") 
    