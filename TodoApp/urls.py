from django.urls import path
from . import views
from .views import ListaTareas, DetallesTarea, CrearTarea, EditarTarea, EliminarTarea

urlpatterns = [
    path('', ListaTareas.as_view(), name='tareas'),
    path('tarea/<int:pk>/', DetallesTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('edi/<int:pk>/', EditarTarea.as_view(), name='editar-tarea'),
    path('elitar-tareaminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar-tarea'),
]