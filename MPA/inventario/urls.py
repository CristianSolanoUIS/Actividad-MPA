from django.urls import path

from . import views


urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.listarProductos, name='listarProductos'),
    path('restar/',views.restarStock, name='restarStock'),
    path('sumar/',views.sumarStock, name='sumarStock')
]

