from django import forms

class formulario(forms.Form): #Curso form, es un formulario porque hereda de formulario.
    id=forms.IntegerField()
    nombre = forms.CharField(max_length=50) 
    email = forms.EmailField()
    