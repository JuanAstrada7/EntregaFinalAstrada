from django.shortcuts import render
from django.http import HttpResponse
from .models import Piloto, Carrera, Puntos
from .forms import PilotoForm, CarreraForm, PuntosForm, RegistrarUsuario, EditarUsuario
from django.db.models import Sum
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def inicio(request):

    return render(request, "F1App/inicio.html")


def inicio_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST) 

        if formulario.is_valid():
            
            info = formulario.cleaned_data 

            usuario = info["username"]
            contra = info["password"]

            usuario_actual = authenticate(username=usuario, password=contra) 

            if usuario_actual is not None: 
                login(request, usuario_actual) 

                return render(request,"F1App//inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
        else: 

            return render(request, "F1App/inicio.html", {"mensaje":"error, datos incorrectos"})
    
    else:

        formulario = AuthenticationForm()

    return render(request, "F1App/inicio_sesion.html", {"formu":formulario})


def cerrar_sesion(request):
    logout(request)

    return render(request,"F1App/cerrar_sesion.html")


def registro(request):

    if request.method == "POST": 

         #formulario = RegistrarUsuario(request.POST) #tengo la información
         formulario = UserCreationForm(request.POST) 

         if formulario.is_valid():
             
             info = formulario.cleaned_data

             usuario = info["first_name"] 

             formulario.save()

             return render(request,"F1App/inicio.html", {"mensaje":f"Bienvenido {usuario}"})


    #formulario = RegistrarUsuario()
    formulario = UserCreationForm()

    return render(request, "F1App/registrar_usuario.html", {"formu":formulario})


def editar_perfil(request):

    usuario_actual =request.user 

    if request.method == "POST": 

         #formulario = EditarUsuario(request.POST) 
         formulario = UserCreationForm(request.POST)

         if formulario.is_valid():
             
             info = formulario.cleaned_data

             usuario_actual.first_name = info["first_name"]
             usuario_actual.last_name = info["last_name"]
             usuario_actual.email = info["email"]
             usuario_actual.set_password(info["password1"]) 

             usuario_actual.save()

             return render(request,"F1App/inicio.html")

    else:
        #formulario = EditarUsuario(initial={"first_name": usuario_actual.first_name,
                                                #"last_name": usuario_actual.last_name,
                                                #"email": usuario_actual.email})
        formulario = UserCreationForm(initial={"first_name": usuario_actual.first_name,
                                                "last_name": usuario_actual.last_name,
                                                "email": usuario_actual.email}) 

    return render(request, "F1App/editar_usuario.html", {"formu":formulario})

def agregar_piloto(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            return render('F1App/inicio.html')  # Reemplaza 'nombre_de_tu_vista' con el nombre correcto
    else:
        form = PilotoForm()
    return render(request, 'f1app/agregar_piloto.html', {'form': form})        

def crear_piloto(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            return render('F1App/inicio.html')
    else:
        form = PilotoForm()
    return render(request, 'F1App/formu_piloto.html', {'form': form})


def ver_piloto(request):

    misPilotos = Piloto.objects.all() 

    info = {"pilotos":misPilotos}

    return render(request, "F1App/pilotos.html", info)

def actualizar_piloto(request, piloto_nombre):

    pilotoElegido = Piloto.objects.get(nombre=piloto_nombre)

    if request.method == "POST":

        nuevo_formulario = PilotoForm(request.POST) 

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data 

            pilotoElegido.nombre = info["nombre"]
            pilotoElegido.equipo = info["equipo"]

            pilotoElegido.save()

            return render(request, "F1App/inicio.html") 
    
    else: 

        nuevo_formulario  = PilotoForm(initial={"nombre": pilotoElegido.nombre,
                                                     "año":pilotoElegido.equipo}) 

    return render(request, "F1App/update_piloto.html", {"mi_formu":nuevo_formulario})


def eliminar_piloto(request, piloto_nombre):

   
    pilotoElegido = Piloto.objects.get(nombre=piloto_nombre) 

    pilotoElegido.delete()

    return render(request, "F1App/pilotos.html")


def ver_carrera(request):

    misCarreras = Carrera.objects.all() 

    info = {"pilotos":misCarreras}

    return render(request, "F1App/carreras.html", info)


def crear_carrera(request):
    if request.method == 'POST':

        nuevoform = CarreraForm(request.POST)

        if nuevoform.is_valid():

            info = nuevoform.cleaned_data

            serie_nueva = Carrera(piloto=info["piloto"], posicion=info["posicion"], vuelta_rapida=info["vuelta rapida"])

            nuevoform.save()
            return render('F1App/inicio.html')
    else:
        nuevoform = PilotoForm()
    return render(request, 'F1App/crear_carrera.html', {'form': nuevoform})


class CrearCarrera(CreateView):

    model = Carrera
    template_name = "F1App/crear_carrera.html"
    fields = ["piloto", "posicion","vuelta_rapida"]
    success_url = "/listaCarreras/"


class ListaCarreras(ListView):

    model = Carrera
    template_name = "F1App/lista_carrera.html"


class ActualizarCarrera(UpdateView):

    model = Carrera
    template_name = "F1App//crear_carreras.html"
    fields = ["piloto", "posicion","vuelta_rapida"]
    success_url = "/lista_carrera/"


class EliminarCarrera(DeleteView):

    model = Carrera
    template_name = "F1App//borrar_carrera.html"
    success_url = "/lista_carrera/"


def tabla_puntos(request):
    pilotos = Piloto.objects.all()
    equipos = set(piloto.equipo for piloto in pilotos)

    tabla_pilotos = []
    tabla_equipos = []

    for piloto in pilotos:
        puntos_totales = Puntos.objects.filter(carrera__piloto=piloto).aggregate(total_puntos=Sum('puntos'))['total_puntos']
        tabla_pilotos.append({'piloto': piloto, 'puntos': puntos_totales})

    for equipo in equipos:
        puntos_totales = Puntos.objects.filter(carrera__piloto__equipo=equipo).aggregate(total_puntos=Sum('puntos'))['total_puntos']
        tabla_equipos.append({'equipo': equipo, 'puntos': puntos_totales})

    context = {'tabla_pilotos': tabla_pilotos, 'tabla_equipos': tabla_equipos}
    return render(request, 'F1App/tabla_puntos.html', context)


def busqueda_piloto_por_equipo(request):

    return render(request, "F1App/buscar_piloto_equipo.html")


def resultados_buscar_piloto_equipo(request):

    if request.method=="GET":

        equipo_pedido = request.GET["año"]
        resultados_pilotos = Piloto.objects.filter(equipo__icontains=equipo_pedido)


        return render(request, "F1App/buscar_piloto_equipo.html", {"piloto":resultados_pilotos})

    else:
        return render(request, "F1App/buscar_piloto_equipo.html")
