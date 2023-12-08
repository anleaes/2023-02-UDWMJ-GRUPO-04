from django.db import models
from payment.models import Payment
from clients.models import Clients
# Create your models here.

class Reserve(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    reserve_item = models.ManyToManyField(Payment, through='ReserveItem', blank=True)
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reserva'
        reserving =['-created_on']

    def __str__(self):
        return "%s" % (self.total_price) 


class ReserveItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de reserva'
        verbose_name_plural = 'Itens de reservas'
        reserving =['id']

    def __str__(self):
        return "%s" % (self.quantity) 
