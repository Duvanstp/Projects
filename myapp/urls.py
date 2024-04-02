from django.urls import path
from . import views # importo desde la ruta actual views


# aquí quiero tener las url propias de esta app llamada myapp
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.Hello),
    path('projects/', views.projects),
    # path('tasks/<str:title>', views.tasks), ejemplo de como enviar info en la url
    path('tasks/', views.tasks),
    path('create_task/', views.create_task)
]