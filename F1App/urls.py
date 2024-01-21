from django.urls import path
from django import views
from .views import tabla_puntos
from . import views
from F1App.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", inicio, name="Inicio"),


    path("login/", inicio_sesion, name="Iniciar Sesion"),
    path("signup/", registro, name="Registrar Usuario"),
    path("logout/", cerrar_sesion, name= "Cerrar Sesion"),
    path("edit/", editar_perfil, name="Editar Perfil" ), #no se visualiza

    path("lista_carrera/", ListaCarreras.as_view(), name= "Lista de Carreras"), #no se visualiza
    path("crear_carrera/", CrearCarrera.as_view(), name= "Crear Carreras"),
    path("actualizar_carrera/<int:pk>", ActualizarCarrera.as_view(), name= "Actualizar Carreras"),
    path("borrar_carrera/<int:pk>", EliminarCarrera.as_view(), name="Borrar Carreras"),



    path('tablaPuntos/', tabla_puntos, name='Tabla de Puntos'),
    path("agregarPiloto/", crear_piloto, name='Agregar Piloto'),
    path("agregarCarrera/", crear_carrera, name='Agregar Carrera'),


    #Urls de los modelos creados
    path("pilotos/", ver_piloto, name="Pilotos"),
    path("carrera/", ver_carrera, name="Carreras"),


    #URLs para buscar datos
    path("buscarPilotoEquipo/", busqueda_piloto_por_equipo, name="Buscar Piloto"),
    path("resultadoPilotos/", resultados_buscar_piloto_equipo, name = "Resultado Busqueda"), #no se visualiza


    #URLs para actualizar 
    path("actualizarPiloto/<piloto_nombre>", actualizar_piloto, name="Actualizar Piloto"),


    #URLs para eliminar
    path("eliminarPiloto/<piloto_nombre>", eliminar_piloto, name="Eliminar Piloto"),


]