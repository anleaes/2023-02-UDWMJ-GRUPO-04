from django.db import models

# Create your models here.

class TipoVeiculos(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Type_vehicles'
        verbose_name_plural = 'Types_vehicles'
        ordering =['id']

    def __str__(self):
        return self.name