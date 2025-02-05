from django.contrib import admin

#Importanto o models para reconhecer a classe aluno.
from .models import Alunos, Contato

# Register your models here.
admin.site.register(Alunos)
admin.site.register(Contato)