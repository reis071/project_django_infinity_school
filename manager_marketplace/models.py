from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=40)

    def __str__(self):
        return self.nome_categoria
    

class Produto(models.Model):
    nome_produto = models.CharField(max_length=40)
    preco_produto = models.FloatField()
    img_url = models.ImageField(upload_to='manager_marketplace/image/%y/%M/%d')
    data_validade = models.DateField(auto_now=True)
    categoria = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dono = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome_produto