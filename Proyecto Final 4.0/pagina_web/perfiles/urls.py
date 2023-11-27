from django.contrib import admin
from django.urls import path
from perfiles.views import registro, inicio_sesion, MiPerfilUpdateView, CustomLogoutView, agregar_avatar

urlpatterns = [ 
    path('signup/', registro, name="registro"),
    path('login/', inicio_sesion, name='login'),
    path('profile/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
]