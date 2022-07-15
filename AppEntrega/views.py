from django.http import HttpResponse
from django.shortcuts import render
from AppEntrega.models import cliente
from AppEntrega.forms import formulario
from AppEntrega.models import *



# Create your views here.

def principal(request):

    return render(request, "AppEntrega/inicio.html")

def main(request):

    return render(request, "AppEntrega/inicio.html")

def clientes(request):

    return render(request, "AppEntrega/clientes.html")

def empleados(request):

    return render(request, "AppEntrega/empleado.html")

def proveedores(request):

    return render(request, "AppEntrega/proveedores.html")

def clienteFormulario(request): ## ESTO ES PARA DJANGO
    if (request.method=="POST"): ##Ahora no va a traer datos, sino va a traer un formulario.
        form=formulario(request.POST) ##Creo una variable, para recibir el formulario.
        print(form) #lo imprime
        if form.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= form.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            nombre=info["nombre"]
            id=info["id"]
            email=info["email"]
            Cliente= cliente(nombre=nombre, id=id, email=email)
            Cliente.save() ##lo guardas en caso de que sea valido.
            return render (request, "AppEntrega/inicio.html")
    else: #Si no viene por POST
        form=formulario() #Creo el formulario vacio
    return render(request, "AppEntrega/clienteFormulario.html", {"form":form})##lo renderizo y se lo mando como un diccionario para que lo pueda usar mi pantalla, mi template, como una variable.
    ##formulario de arriba tiene que ser el mismo que aparece en el html para usar

def empleadoFormulario(request): ## ESTO ES PARA DJANGO
    if (request.method=="POST"): ##Ahora no va a traer datos, sino va a traer un formulario.
        form=formulario(request.POST) ##Creo una variable, para recibir el formulario.
        print(form) #lo imprime
        if form.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= form.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            nombre=info["nombre"]
            id=info["id"]
            email=info["email"]
            Empleado= empleado(nombre=nombre, id=id, email=email)
            Empleado.save() ##lo guardas en caso de que sea valido.
            return render (request, "AppEntrega/inicio.html")
    else: #Si no viene por POST
        form=formulario() #Creo el formulario vacio
    return render(request, "AppEntrega/empleadoFormulario.html", {"form":form})##lo renderizo y se lo mando como un diccionario para que lo pueda usar mi pantalla, mi template, como una variable.
    ##formulario de arriba tiene que ser el mismo que aparece en el html para usar

def proveedorFormulario(request): ## ESTO ES PARA DJANGO
    if (request.method=="POST"): ##Ahora no va a traer datos, sino va a traer un formulario.
        form=formulario(request.POST) ##Creo una variable, para recibir el formulario.
        print(form) #lo imprime
        if form.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= form.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            nombre=info["nombre"]
            id=info["id"]
            email=info["email"]
            Proveedor= proveedor(nombre=nombre, id=id, email=email)
            Proveedor.save() ##lo guardas en caso de que sea valido.
            return render (request, "AppEntrega/inicio.html")
    else: #Si no viene por POST
        form=formulario() #Creo el formulario vacio
    return render(request, "AppEntrega/proveedorFormulario.html", {"form":form})##lo renderizo y se lo mando como un diccionario para que lo pueda usar mi pantalla, mi template, como una variable.
    ##formulario de arriba tiene que ser el mismo que aparece en el html para usar


def busquedaCliente(request):
    return render(request, "AppEntrega/busquedaCliente.html")

def buscar(request):
    if request.GET["nombre"]: ## Si tenes algo en nombre, lo busca en el nombre de busquedacliente, por eso despues aparece en la URL ese GET
        busqueda= request.GET["nombre"]
        respuesta_busqueda = cliente.objects.filter(nombre=busqueda)
        return render (request, "AppEntrega/resultadosBusqueda.html" ,{"respuesta_busqueda":respuesta_busqueda})
    else:
        return render(request, "AppEntrega/busquedaCliente.html", {"Error":"No se ingreso ningun nombre"})