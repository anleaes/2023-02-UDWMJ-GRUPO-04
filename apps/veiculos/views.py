from django.shortcuts import render, get_object_or_404, redirect
from .forms import VeiculoForm
from .models import Veiculo

# Create your views here.

def add_veiculo(request):
    template_name = 'veiculos/add_veiculo.html'
    context = {}
    if request.method == 'POST':
        form = VeiculoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('veiculos:list_veiculos')
    form = VeiculoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_veiculos(request):
    template_name = 'veiculos/list_veiculos.html'
    veiculos = Veiculo.objects.filter()
    context = {
        'veiculos': veiculos
    }
    return render(request, template_name, context)

def edit_veiculo(request, id_veiculo):
    template_name = 'veiculos/add_veiculo.html'
    context ={}
    veiculo = get_object_or_404(Veiculo, id=id_veiculo)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, request.FILES,  instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculos:list_veiculos')
    form = VeiculoForm(instance=veiculo)
    context['form'] = form
    return render(request, template_name, context)

def delete_veiculo(request, id_veiculo):
    veiculo = Veiculo.objects.get(id=id_veiculo)
    veiculo.delete()
    return redirect('veiculos:list_veiculos')