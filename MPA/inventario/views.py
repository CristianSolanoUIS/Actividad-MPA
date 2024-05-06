from django.shortcuts import redirect,get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

from .forms import ProductoForm
from .models import Producto

# Vista principal de Productos
def listarProductos(request):
    
    #consultar productos
    productos = Producto.objects.all()

    #Obtener el template
    template = loader.get_template("listarProductos.html")
    #Agregar el contexto
    context = {"productos":productos}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un autor
def sumarStock(request):

    #Obtener el template
    template = loader.get_template("sumarStock.html")  

    if request.method == "POST": 
        form = ProductoForm(request.POST or None, request.FILES)
        if form.is_valid():
            productoVigente = form.save(commit=False)

            cantidadActualizada = form.cleaned_data.get('cantidad') 
            
            productoVigente.tipo_cambio = 'Ingreso'
            productoVigente.fecha = datetime.now()

            productoActualizado = productoVigente.id_producto

            productoActualizado.cantidad += cantidadActualizada
            productoActualizado.save()
            productoVigente.save()

            return redirect("listarProductos")
    else: 
        form = ProductoForm()

    #Consultar datos de producto
    context = {}
    context['form'] = form

    return HttpResponse(template.render(context,request))

def restarStock(request):
    # Obtener el template
    template = loader.get_template("restarStock.html")

    if request.method == "POST": 
        form = ProductoForm(request.POST or None, request.FILES)
        if form.is_valid():
            productoVigente = form.save(commit=False)
            cantidadActualizada = form.cleaned_data.get('cantidad') 
            
            if cantidadActualizada <= productoVigente.id_producto.cantidad:
                productoVigente.tipo_cambio = 'Egreso'
                productoVigente.fecha = datetime.now()
                productoActualizado = productoVigente.id_producto
                productoActualizado.cantidad -= cantidadActualizada
                productoActualizado.save()
                productoVigente.save()
                return redirect("listarProductos")
        
        # Si la cantidad es mayor que la disponible, mostrar mensaje de error
        form = ProductoForm(request.POST or None, request.FILES)
        context = {'form': form, 'error_message': 'Cantidad inconsistente'}
        return HttpResponse(template.render(context, request))
        
    else: 
        form = ProductoForm()

    # Consultar datos de producto
    context = {'form': form}

    return HttpResponse(template.render(context, request))
