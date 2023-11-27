from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(auto_now = True)
    destacado = models.BooleanField(default=False)
    #imagen
    def __str__(self):
        return f"{self.titulo}, de {self.autor}"