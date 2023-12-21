from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self): # para que aparezca el nombre del proyecto cuando se llama
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200) # creamos campo más extenso que charfield
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # relacion con la tabla de Project
    # el on_delete es para que hace si se elimina un proyecto y el models.CASCADE es para que se eliminen dependencias en cascada
    done = models.BooleanField(default = False)
    def __str__(self):
        return self.title + ' - ' + self.project.name