from django.shortcuts import render, get_object_or_404, redirect
from .forms import RentalcompanyForm
from .models import Rentalcompany

# Create your views here.
def add_rentalcompany(request):
    template_name = 'rentalcompany/add_rentalcompany.html'
    context = {}
    if request.method == 'POST':
        form = RentalcompanyForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('rentalcompany:list_rentalcompany')
    form = RentalcompanyForm()
    context['form'] = form
    return render(request, template_name, context)

def list_rentalcompany(request):
    template_name = 'rentalcompany/list_rentalcompany.html'
    rentalcompany = Rentalcompany.objects.filter()
    context = {
        'rentalcompany': rentalcompany
    }
    return render(request, template_name, context)

def edit_rentalcompany(request, id_rentalcompany):
    template_name = 'rentalcompany/add_rentalcompany.html'
    context ={}
    rentalcompany = get_object_or_404(Rentalcompany, id=id_rentalcompany)
    if request.method == 'POST':
        form = RentalcompanyForm(request.POST, request.FILES,  instance=rentalcompany)
        if form.is_valid():
            form.save()
            return redirect('rentalcompany:list_rentalcompany')
    form = RentalcompanyForm(instance=rentalcompany)
    context['form'] = form
    return render(request, template_name, context)

def delete_rentalcompany(request, id_rentalcompany):
    rentalcompany = Rentalcompany.objects.get(id=id_rentalcompany)
    rentalcompany.delete()
    return redirect('rentalcompany:list_rentalcompany')