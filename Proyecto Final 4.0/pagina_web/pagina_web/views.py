from django.shortcuts import render
from articulos.models import Articulo

def inicio(request):
    # Recupera artículos destacados para mostrar en la página de inicio
    articulos_destacados = Articulo.objects.filter(destacado=True)[:3]  # Cambia el filtro según tus criterios

    return render(request, 'inicio.html', {'articulos_destacados': articulos_destacados})

def about_me(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='about_me.html',
        context=contexto,
    )
    return http_response