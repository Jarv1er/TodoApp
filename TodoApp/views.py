from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea

# Create your views here.

class IniciarSesion(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("tareas")


class ListaTareas(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = "tareas"
    template_name = 'TodoApp/lista_tareas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completado=False).count()
        return context
    


class DetallesTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = 'TodoApp/tarea.html'


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ["titulo", "descripcion", "completado"]
    success_url = reverse_lazy("tareas")

    def form_valid(self, form):
        return super(self, CrearTarea).form_valid(form)


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ["titulo", "descripcion", "completado"]
    success_url = reverse_lazy("tareas")


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = "tareas"
    template_name = 'TodoApp/elimnar_tarea.html'
    success_url = reverse_lazy("tareas")
