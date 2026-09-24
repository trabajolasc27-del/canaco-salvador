from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("noticia/", views.detalle_noticia, name="detalle"),
    path("categoria/", views.categoria, name="categoria"),
    path("iniciar-sesion/", views.login_view, name="login"),
    path("registro/", views.registro, name="registro"),
]