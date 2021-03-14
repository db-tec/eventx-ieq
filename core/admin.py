from django.contrib import admin
from .models import Evento, Inscricao

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','descricao','data_inicial', 'quantidade','criado', 'ativo')

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'sobrenome', 'telefone', 'email', 'evento', 'criado')
    list_filter = ['evento']
    search_fields = ['nome', 'sobrenome']


class StackedItemInline(admin.StackedInline):
    classes = ('grp-collapse grp-open',)

class TabularItemInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
