from django.shortcuts import render

def inicio(request, exception=None):
    return render(request, "inicio/inicio.html", {})
