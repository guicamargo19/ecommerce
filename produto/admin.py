from django.contrib import admin
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    list_display = ('nome', 'descricao_curta', 'descricao_longa',
                    'preco_marketing', 'preco_marketing_promocional', 'tipo')
    ordering = '-id',
    list_filter = 'nome', 'tipo',
    list_editable = 'tipo',
    inlines = [VariacaoInline]
