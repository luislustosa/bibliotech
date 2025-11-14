from django.contrib import admin
from .models import Autor, Editora, Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editora', 'genero', 'isbn')
    list_filter = ('autor', 'editora', 'genero') 
    search_fields = ('titulo', 'isbn', 'autor__nome', 'editora__nome')

admin.site.register(Autor)
admin.site.register(Editora)
