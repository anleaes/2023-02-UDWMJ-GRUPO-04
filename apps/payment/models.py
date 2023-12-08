from django.db import models

# Create your models here.
class Product(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type_payment = models.CharField('Forma de Pagamento', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    status = models.BooleanField('Em Aberto', default=False)
    
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering =['id']

    def __str__(self):
        return self.name