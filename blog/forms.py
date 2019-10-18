from django import forms
from .models import Post
#IMPORTO LA CLASE PERSONA
from .models import Persona

"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        """
class PostForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('apellido', 'nombre', 'dni', 'domicilio', 'fechaDeNacimiento' ,)
