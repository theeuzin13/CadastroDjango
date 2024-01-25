from django.urls import path
#As funções ficam sempre dentro do arquivo view do app
from app_cad_usuario import views


urlpatterns = [
    #rota, view responsável e nome de referência
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]
