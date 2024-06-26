from django.contrib import admin
from .models import Produto,Categoria

# Register your models here.
@admin.register(Produto)
class adminProduto(admin.ModelAdmin):
    ...

@admin.register(Categoria)
class adminProduto(admin.ModelAdmin):
    ...

