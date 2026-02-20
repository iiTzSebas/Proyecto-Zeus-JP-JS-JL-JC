from django.http import HttpResponse

from django.shortcuts import render

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