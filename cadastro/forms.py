from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    #Classe padrão que define quais campos iremos usar
    class Meta:
        #Informa o modelo
        model = Contato

        #Informa os campos
        fields = ['nome', 'email', 'mensagem']

        #Define como as labels apareceram no formulario
        labels = {
            'nome': 'Nome completo:',
            'email': 'Informe seu email:',
            'mensagem': 'Digite sua mensagem:'
        }