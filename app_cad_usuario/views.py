from django.shortcuts import render
from .models import  Usuario

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvar os dados da tela no banco de dados, pegando do html
    novo_usuario =  Usuario()
    novo_usuario.nome = request.POST.get('Nome')
    novo_usuario.idade = request.POST.get('Idade')
    novo_usuario.save()

    #Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
