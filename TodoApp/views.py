from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Tarea

# Create your views here.


class ListaTareas(ListView):
    model = Tarea
    context_object_name = "tareas"
    template_name = 'TodoApp/lista_tareas.html'


class DetallesTareas(DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = 'TodoApp/tarea.html'


class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy("tareas")