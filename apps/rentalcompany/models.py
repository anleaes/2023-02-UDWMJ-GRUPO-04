from django.db import models

# Create your models here.
class Rentalcompany(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    address = models.TextField('Endereço', max_length=200)
    cell_phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    
    class Meta:
        verbose_name = 'Locadora'
        verbose_name_plural = 'Locadoras'
        ordering =['id']

    def __str__(self):
        return self.name
