from django.shortcuts import render, get_object_or_404, redirect
from .forms import MotoristaForm
from .models import Motorista

# Create your views here.

def add_motorista(request):
    template_name = 'motoristas/add_motorista.html'
    context = {}
    if request.method == 'POST':
        form = MotoristaForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('motoristas:list_motoristas')
    form = MotoristaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_motoristas(request):
    template_name = 'motoristas/list_motoristas.html'
    motorista = Motorista.objects.filter()
    context = {
        'motorista': motorista
    }
    return render(request, template_name, context)

def edit_motorista(request, id_motorista):
    template_name = 'motoristas/add_motorista.html'
    context ={}
    motorista = get_object_or_404(Motorista, id=id_motorista)
    if request.method == 'POST':
        form = MotoristaForm(request.POST, request.FILES,  instance=motorista)
        if form.is_valid():
            form.save()
            return redirect('motoristas:list_motoristas')
    form = MotoristaForm(instance=motorista)
    context['form'] = form
    return render(request, template_name, context)

def delete_motorista(request, id_motorista):
    motorista = Motorista.objects.get(id=id_motorista)
    motorista.delete()
    return redirect('motoristas:list_motoristas')