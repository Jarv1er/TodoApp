from django.urls import path
from . import views
from .views import ListaTareas, DetallesTarea, CrearTarea, EditarTarea, EliminarTarea, IniciarSesion
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', IniciarSesion.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ListaTareas.as_view(), name='tareas'),
    path('tarea/<int:pk>/', DetallesTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>/', EditarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar-tarea'),
]