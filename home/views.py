from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


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