from django.contrib import admin

from .models import (
    Archivo,
    Categoria,
    Comentario,
    GaleriaPublicacion,
    Perfil,
    Publicacion,
)


admin.site.site_header = "Administración CANACO Tabasco"
admin.site.site_title = "CANACO Tabasco"
admin.site.index_title = "Panel de administración"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "fk_user",
        "createdat",
        "updatedat",
    )

    search_fields = (
        "nombre",
        "fk_user__username",
    )

    ordering = ("nombre",)


@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "tipo",
        "tamano",
        "fk_user",
        "createdat",
    )

    search_fields = (
        "nombre",
        "nombre_temporal",
        "tipo",
    )

    list_filter = (
        "tipo",
        "createdat",
    )


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "categoria",
        "autor",
        "estado",
        "visitas",
        "createdat",
    )

    search_fields = (
        "titulo",
        "resumen",
        "contenido",
        "autor__username",
    )

    list_filter = (
        "estado",
        "categoria",
        "createdat",
    )

    ordering = ("-createdat",)


@admin.register(GaleriaPublicacion)
class GaleriaPublicacionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "publicacion",
        "archivo",
        "createdat",
    )

    search_fields = (
        "publicacion__titulo",
        "archivo__nombre",
    )


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "publicacion",
        "estado",
        "createdat",
        "updatedat",
    )

    search_fields = (
        "contenido",
        "user__username",
        "publicacion__titulo",
    )

    list_filter = (
        "estado",
        "createdat",
    )

    ordering = ("-createdat",)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "apellido_paterno",
        "apellido_materno",
        "foto_perfil",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "apellido_paterno",
        "apellido_materno",
    )