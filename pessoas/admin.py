from django.contrib import admin
from .models import Pessoa


class ListandoPessoas(admin.ModelAdmin):
    list_display = ('nome', 'email') # exibe esses campos no admin
    list_display_links = ['nome'] # campos com link para clicar e editar a receita
    search_fields = ['nome'] # Campos para campos de busca
    list_per_page = 2 # cria uma paginação por qtde de receitas


# Register your models here.
admin.site.register(Pessoa, ListandoPessoas)