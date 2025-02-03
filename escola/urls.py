"""
URL configuration for escola project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Aqui informamaos quais funções temos na views
from cadastro.views import alunos_list, alunos_contato

urlpatterns = [
    path('admin/', admin.site.urls),

    #aqui definmos o nome da pagina que sera acessada no navegador e qual função da view sera chamada
    #Ob serve que neste patch o local do nome deixei vazio, Isso significa que esta é a nossa pagina inicial
    path('', alunos_list,name='home'),

    #Aqui definimos a pagina contato
    path('contato/', alunos_contato,name='contato')
]
