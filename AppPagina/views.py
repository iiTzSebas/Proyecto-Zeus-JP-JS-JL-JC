from django.http import HttpResponse

from django.shortcuts import render

from.models import estudiante

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
    return render(request, "estudiantes/crear.html") 

def editar(request):
    return render(request, "estudiantes/editar.html") 
    