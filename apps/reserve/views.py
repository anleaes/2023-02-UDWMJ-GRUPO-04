
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReserveForm, ReserveItemForm
from .models import Reserve , ReserveItem, Payment, Clients
# Create your views here.
def add_reserve(request, id_clients):
    template_name = 'reserve/add_reserve.html'
    context = {}
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.clients = Clients.objects.get(id=id_clients)
            f.save()
            form.save_m2m()
            return redirect('reserve:list_reserve')
    form = ReserveForm()
    context['form'] = form
    return render(request, template_name, context)

def list_reserve(request):
    template_name = 'reserve/list_reserve.html'
    reserve = Reserve.objects.filter()
    reserve_items = ReserveItem.objects.filter()
    payment = Payment.objects.filter()
    clients = Clients.objects.filter()
    context = {
        'reserve': reserve,
        'reserve_items': reserve_items,
        'payment': payment,
        'clients': clients
    }
    return render(request, template_name, context)

def delete_reserve(request, id_reserve):
    reserve = Reserve.objects.get(id=id_reserve)
    reserve.delete()
    return redirect('reserve:list_reserve')

def add_reserve_item(request, id_reserve):
    template_name = 'reserve/add_reserve_item.html'
    context = {}
    if request.method == 'POST':
        form = ReserveItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.reserve = Reserve.objects.get(id=id_reserve)
            f.save()
            form.save_m2m()
            return redirect('reserve:list_reserve')
    form = ReserveItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_reserve_item(request, id_reserve_item):
    reserveitem = ReserveItem.objects.get(id=id_reserve_item)
    reserveitem.delete()
    return redirect('reserve:list_reserve')

def edit_reserve_status(request, id_reserve):
    template_name = 'reserve/edit_reserve_status.html'
    context ={}
    reserve = get_object_or_404(Reserve, id=id_reserve)
    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=reserve)
        if form.is_valid():
            form.save()
            return redirect('reserve:list_reserve')
    form = ReserveForm(instance=reserve)
    context['form'] = form
    return render(request, template_name, context)