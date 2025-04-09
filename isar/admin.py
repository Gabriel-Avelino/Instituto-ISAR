from django.contrib import admin
from .models import Documento, Tipo, Estado, Cidade, Bairro, Regiao, Imovel, ImagemImovel, Tipo_Doc

# Register your models here.
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('name_doc', 'tipo')  # Campos visíveis na listagem
    list_filter = ('tipo',)  # Adiciona filtro por tipo
    search_fields = ('name_doc', 'tipo__name')  # Adiciona campo de busca

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Tipo)
admin.site.register(Imovel)
admin.site.register(ImagemImovel)
admin.site.register(Tipo_Doc)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Regiao)