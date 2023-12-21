from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
 # para crear respuestas al servidor como strings

from .models import Project, Task # nota no olvide el punto antes de model

from django.shortcuts import get_object_or_404, render # manejo de errores de no existe en la db

# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request, "index.html",
                  {'title': title}
                  ) # el render llama al archivo dentro de templates, se debe pasar el request a la funcion render

def Hello(request, username):
    return HttpResponse("<h1> Hello %s!! <h1>"%username) # %s concatena el str username al texto

def about(request):
    username = 'Duvan'
    return render(request, "about.html",
                  {
                      "username":username
                  })

def projects(request):
    projects = Project.objects.all() # primer query obtiene los valores 
    # projects = list(projects)
    return render(request, "projects.html" , 
                  {
                      'projects': projects
                  })
    # return JsonResponse(projects, safe=False) # ahora usamos json para devolver info

def tasks(request): # le puedo pasar el parametro title o id para que busque por el moemnto no quiero eso
    # task = Task.objects.get(id = id) metodo normal Tambien se puede buscar por otro atributo
    # task = get_object_or_404(Task, title = title) # método evitar error de not found
    # return HttpResponse("task: %s" %task.title)
    tasks = Task.objects.all()
    return render(request, "tasks.html",
                  {
                      'tasks': tasks
                  })