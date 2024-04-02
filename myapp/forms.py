from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label = 'Descripcion de task', required = False) # para poder usar el chrafiel como text area
