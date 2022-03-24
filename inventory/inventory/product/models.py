from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length = 35, verbose_name='Item name')
    price =  models.IntegerField()
    detail = models.TextField()
    quantity = models.IntegerField()
    class Meta:
        ordering=['id']
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id}.)   {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('Product:form_success')