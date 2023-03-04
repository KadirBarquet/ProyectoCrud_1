from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm
from django.db.models import Q
 

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def listar_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(id__icontains=query) | Q(nombre__icontains=query)
        )
    else:
        productos = Producto.objects.all()
    
    return render(request, 'ropa/index.html', {'productos': productos})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ropa')
    else:
        form = ProductoForm()
    return render(request, 'ropa/crear.html', {'formulario': form})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ropa')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ropa/editar.html', {'formulario': form})


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('ropa')