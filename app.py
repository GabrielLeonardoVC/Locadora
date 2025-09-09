import os
from classes import *
from funcoes import *
while True:
    try:
        os.system("cls")
        input(" ______________________________\n |                            |\n |                            |\n |     Sistema de locação     |\n |                            |\n |____________________________|\n\nSistema de Locação a seguir.\nClique em qualquer tecla para continuar... ")
        os.system("cls")
        print("1º Cadastrar Cliente")
        print("2º Listar Clientes")
        print("3º Cadastrar Item (Filme/Jogo)")
        print("4º Listar Itens")
        print("5º Sair")
        escolha = int(input("-->"))
        os.system("pause")

        match escolha:
            case 1:
                cadastrarocliente()
                os.system("cls")
            case 2:
                listaroclientes()
                os.system("cls")
            case 3:
                cadastroItem()
                os.system("cls")
            case 4:
                listarItens()
                os.system("cls")
            case 5:
                print("Saindo...")
                os.system("pause")
                break
            case _:
                print("Opção inválida!")
                os.system("pause")

    except Exception as e:
        print("Ocorreu um erro inesperado")
        os.system("pause")