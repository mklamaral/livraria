from django.contrib import admin
from .models import Autor, Categoria, Editora, Livro, Compra, ItensCompra


# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")
    list_filter = ("nome",)
    ordering = ("nome", "email")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)


class ItensCompraOnline(admin.TabularInline):
    model = ItensCompra
    extra = 1
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "status")
    ordering = ("-id",)
    list_per_page = 25
    inlines = [ItensCompraOnline]


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = ("nome",)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "editora", "categoria")
    search_fields = ("titulo", "editora__nome", "categoria__descricao")
    list_filter = ("editora", "categoria")
    ordering = ("titulo", "editora", "categoria")
    list_per_page = 25
