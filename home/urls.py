from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("noticia/", views.detalle_noticia, name="detalle"),
    path("categoria/", views.categoria, name="categoria"),
    path("iniciar-sesion/", views.login_view, name="login"),
    path("registro/", views.registro, name="registro"),
    path("perfil/", views.perfil, name="perfil"),
    path("panel/", views.panel, name="panel"),
    path("panel/noticias/", views.panel_noticias, name="panel_noticias"),
    path("panel/publicacion/nueva/", views.nueva_publicacion, name="nueva_publicacion"),
    path(
    "panel/comentarios/",
    views.panel_comentarios,
    name="panel_comentarios",
),
path(
    "panel/categorias/",
    views.panel_categorias,
    name="panel_categorias",
),
path(
    "panel/usuarios/",
    views.panel_usuarios,
    name="panel_usuarios",
),
]