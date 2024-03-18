from django.contrib import admin
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    list_display = ('nome', 'descricao_curta',
                    'get_preco_formatado', 'get_preco_promo_formatado',)
    ordering = '-id',
    list_filter = 'nome', 'tipo',
    inlines = [VariacaoInline]
