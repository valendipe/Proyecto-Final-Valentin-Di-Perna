from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from articulos.models import Articulo
from articulos.forms import ArticulosInsertar
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class ArticuloListView(ListView):
   model = Articulo
   template_name = 'articulos/listar_articulos.html'

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo')
    success_url = reverse_lazy('lista_articulos')
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.autor = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('lista_articulos')

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('lista_articulos')

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo')
    success_url = reverse_lazy('lista_articulos')

