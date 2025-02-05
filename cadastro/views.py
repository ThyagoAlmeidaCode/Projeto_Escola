from django.shortcuts import render, redirect

#Importa o modelo de alunos
from .models import Alunos, Contato
from .forms import ContatoForm

#Função que rendereiza a pagina html com os dados dos alunos
def alunos_list(request):        
    alunos_list = Alunos.objects.all()   
    return render(request, 'cadastro/alunos_list.html', {"alunos": alunos_list})

def alunos_contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #Informa como o formulario sera criado
        formulario = ContatoForm()
        return render(request, 'cadastro/alunos_contato.html', {'form':formulario})