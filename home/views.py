from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")

def noticias(request):
    return render(request, "home/noticias.html")

def detalle_noticia(request):
    return render(request, "home/detalle.html")


def categoria(request):
    return render(request, "home/categoria.html")


def login_view(request):
    return render(request, "home/login.html")


def registro(request):
    return render(request, "home/registro.html")

def perfil(request):
    return render(request, "home/perfil.html")


def panel(request):
    return render(request, "home/panel.html")

def panel_noticias(request):
    return render(request, "home/panel_noticias.html")


def nueva_publicacion(request):
    return render(request, "home/nueva_publicacion.html")

def panel_comentarios(request):
    return render(request, "home/panel_comentarios.html")


def panel_categorias(request):
    return render(request, "home/panel_categorias.html")


def panel_usuarios(request):
    return render(request, "home/panel_usuarios.html")

def cambiar_password(request):
    return render(request, "home/cambiar_password.html")