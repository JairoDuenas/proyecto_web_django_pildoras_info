from django import forms

class FormularioContacto(forms.Form):
  nombre = forms.CharField(label='Nombre', required=True)
  email = forms.CharField(label='Email', max_length=100)
  contenido = forms.CharField(label='Contenido', widget=forms.Textarea(attrs={'cols': 20, 'rows': 5}))