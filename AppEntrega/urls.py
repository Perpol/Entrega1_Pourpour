from threading import main_thread
from django.urls import path
from .views import *


urlpatterns = [
    path('', principal, name="Principal"),
    path('empleados/', empleados, name="Empleados"),
    path('clientes/', clientes, name="clientes"),
    path('proveedores/', proveedores, name="Proveedor"),
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),
    path('empleadoFormulario/', empleadoFormulario, name="empleadoFormulario"),
    path('proveedorFormulario/', proveedorFormulario, name="proveedorFormulario"),
    path('busquedaCliente/', busquedaCliente, name="busquedaCliente"),
    path('buscar/', buscar, name="buscar"),
]
    