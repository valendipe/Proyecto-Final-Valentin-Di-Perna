from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView



def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

def inicio_sesion(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data  # diccionario
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:  # Chequeo usario existe
                login(request=request, user=user)  # creas la sesión al usuario
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='perfiles/login.html',
        context={'form': form},
    )

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'perfiles/perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

class CustomLogoutView(LogoutView):
    template_name = 'inicio.html'
    

def agregar_avatar(request):
  if request.method == "POST":
      formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

      if formulario.is_valid():
          avatar = formulario.save()
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('inicio')
          return redirect(url_exitosa)
  else:  # GET
      formulario = AvatarFormulario()
  return render(
      request=request,
      template_name="perfiles/avatar.html",
      context={'form': formulario},
  )
