import os
from classes import *
Locadoraa = locadora("Locadora")

def cadastrarocliente():
    try:
        input(" ______________________\n |                    |\n |                    |\n |      Cadastro      |\n |                    |\n |____________________|\n\nRealize seu Cadastro a seguir.\nClique em qualquer tecla para continuar... ")
        os.system("cls")
        nome = input("Informe o nome do cliente: ")
        os.system("cls")
        cpf = input("Informe o CPF do cliente: ")
        os.system("cls")
        print("\nCliente cadastrado com sucesso!")
        os.system("pause")
    except Exception as e:
        print ("Ocorreu um erro inesperado")
        os.system ("pause")


def cadastroItem():
    while True:
        os.system("cls")
        input(" ______________________________\n |                            |\n |                            |\n |      Cadastro de item      |\n |                            |\n |____________________________|\n\nRealize seu Cadastro a seguir.\nClique em qualquer tecla para continuar... ")
        tipo=int(input("1º Filme\n2º Jogo\n3º Sair\n-->"))
        if tipo==1:
            idd=int(input("ID do filme:"))
            os.system("cls")
            titulo=input("Título do filme:")
            os.system("cls")
            genero=input("Gênero:")
            os.system("cls")
            Locadoraa.cadastrarFilme(idd,titulo,genero)
            print("\nFilme cadastrado com sucesso!")
            os.system("cls")
            os.system("pause")
            break


        elif tipo==2:
            idd=int(input("ID do jogo:"))
            os.system("cls")
            titulo=input("Nome do jogo:")
            os.system("cls")
            faixa=input("Faixa etária:")
            os.system("cls")
            Locadoraa.cadastrarJogo(idd,titulo,faixa)
            print("\nJogo cadastrado com sucesso!")
            os.system("cls")
            os.system("pause")
            break
        
        elif tipo==3:
            break
        else:
            print("Opção inválida")
            os.system("cls")
            os.system("pause")


def listaroclientes():
    os.system("cls")
    input(" ______________________________\n |                            |\n |                            |\n |      Lista de clientes      |\n |                            |\n |____________________________|\n\nLista dos clientes a seguir.\nClique em qualquer tecla para continuar... ")

    for idd, cliente in Locadoraa.listaroclientes().item():
        print(f"{idd}-{cliente.getNome()}CPF:{cliente.getCpf()}")
        os.system("cls")
    os.system("pause")


def listarItens():
    os.system("cls")
    input(" ___________________________\n |                         |\n |                         |\n |      Lista de itens      |\n |                         |\n |_________________________|\n\nLista de itens a seguir.\nClique em qualquer tecla para continuar... ")

    for idd, item in Locadoraa.listarItem().item():
        status="Disponível" if item.isDisponivel() else "Alugado"
        print(f"{id}-{item.getTitulo()}({status})")
        os.system("cls")
    os.system("pause")


