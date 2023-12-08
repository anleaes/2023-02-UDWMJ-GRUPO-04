from django.shortcuts import render, get_object_or_404, redirect
from .forms import TipoVeiculosForm
from .models import TipoVeiculos

# Create your views here.

def add_tipoveiculos(request):
    template_name = 'tipo_veiculos/add_tipoveiculos.html'
    context = {}
    if request.method == 'POST':
        form = TipoVeiculosForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tipo_veiculos:list_tipo_veiculos')
    form = TipoVeiculosForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tipo_veiculos(request):
    template_name = 'tipo_veiculos/list_tipo_veiculos.html'
    tipo_veiculos = TipoVeiculos.objects.filter()
    context = {
        'tipo_veiculos': tipo_veiculos
    }
    return render(request, template_name, context)

def delete_tipoveiculos(request, id_tipoveiculos):
    tipoveiculos = TipoVeiculos.objects.get(id=id_tipoveiculos)
    tipoveiculos.delete()
    return redirect('tipo_veiculos:list_tipo_veiculos')