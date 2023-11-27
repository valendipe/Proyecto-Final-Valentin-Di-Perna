
from django.urls import path
from articulos.views import *

urlpatterns = [
    path("", ArticuloListView.as_view(), name="lista_articulos"),
    path('pageld/<int:pk>/', ArticuloDetailView.as_view(), name='detalle_articulo'),
    path("create/", ArticuloCreateView.as_view(), name="crear_articulo"),
    path("edit/<int:pk>/", ArticuloUpdateView.as_view(), name="editar_articulo"),
    path("delete/<int:pk>/", ArticuloDeleteView.as_view(), name="eliminar_articulo"),
]
