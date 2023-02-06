from django.shortcuts import render
from .models import Project 

# Create your views here.

def porfolio(request): 
    #obtner lista de proyectos almacenados
    projects= Project.objects.all()  #se le almacene las propiedades del proyecto
    return render(request, "portfolio/porfolio.html",{'projects': projects})