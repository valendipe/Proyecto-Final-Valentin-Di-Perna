from django import forms
from ckeditor.widgets import CKEditorWidget
class ArticulosInsertar(forms.Form):
     titulo = forms.CharField(required=True, max_length=50)
     subtitulo = forms.CharField(required=True, max_length=50)
     cuerpo = forms.CharField(widget=CKEditorWidget(), required=True)