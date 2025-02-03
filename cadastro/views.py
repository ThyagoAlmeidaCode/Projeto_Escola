from django.shortcuts import render

#Importa o modelo de alunos
from .models import Alunos

#Função que rendereiza a pagina html com os dados dos alunos
def alunos_list(request):    
    #Conecta com a base de dados que criamas e tras todos os alunos cadastrados.
    alunos_list = Alunos.objects.all()

    #Aqui a função retorna a pagina alunos_list.html 
    #A pasta cadastro deverá ser criada dentro da pasta templates
    #O arquivo alunos_lsit.html deve ser criada dentro da pasta cadastro
    return render(request, 'cadastro/alunos_list.html', {"alunos": alunos_list})

def alunos_contato(request):
    return render(request, 'cadastro/alunos_contato.html')