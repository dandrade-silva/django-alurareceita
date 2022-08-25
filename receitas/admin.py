from pickletools import markobject
from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'pessoa', 'categoria', 'data_receita', 'publicada') # exibe esses campos no admin
    list_display_links = ('id', 'nome_receita') # campos com link para clicar e editar a receita
    search_fields = ['nome_receita'] # Campos para campos de busca
    list_filter = ['categoria', 'pessoa'] # filtro de categoria
    list_editable = ['publicada'] # campos editaveis antes de abrir o link
    list_per_page = 2 # cria uma paginação por qtde de receitas
    


# Register your models here.
admin.site.register(Receita, ListandoReceitas)