from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm
from .models import Payment

# Create your views here.
def add_payment(request):
    template_name = 'paymnet/add_payment.html'
    context = {}
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('payment:list_payment')
    form = PaymentForm()
    context['form'] = form
    return render(request, template_name, context)

def list_payment(request):
    template_name = 'payment/list_payment.html'
    payment = Payment.objects.filter()
    context = {
        'payment': payment
    }
    return render(request, template_name, context)

def edit_payment(request, id_payment):
    template_name = 'payment/add_payment.html'
    context ={}
    payment = get_object_or_404(Payment, id=id_payment)
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES,  instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment:list_payment')
    form = PaymentForm(instance=payment)
    context['form'] = form
    return render(request, template_name, context)

def delete_payment(request, id_product):
    payment = Payment.objects.get(id=id_product)
    payment.delete()
    return redirect('products:list_payment')