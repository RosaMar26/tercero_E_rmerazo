from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto/',contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),

]