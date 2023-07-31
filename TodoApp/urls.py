from django.urls import path
from . import views
from .views import ListaTareas, DetallesTareas, CrearTarea

urlpatterns = [
    path('', ListaTareas.as_view(), name='tareas'),
    path('tarea/<int:pk>/', DetallesTareas.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
]