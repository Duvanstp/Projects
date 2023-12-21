from django.contrib import admin

# Register your models here.

from .models import Project, Task

admin.site.register(Project)  # agregamos project para que aparezca en el panel de admin
admin.site.register(Task)
