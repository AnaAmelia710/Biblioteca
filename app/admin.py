from django.contrib import admin
from .models import Livro, Autor, Genero, Editora, Cidade, Leitor

admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1  # Quantos livros adicionais aparecem para cadastro


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)         # Mostrar o campo nome na listagem
    search_fields = ('nome',)        # Campo pesquisável
    inlines = [LivroInline]          # Mostrar livros relacionados inline

admin.site.register(Autor, AutorAdmin)
