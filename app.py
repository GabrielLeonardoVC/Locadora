import os
from funcoes import *

while True:
    os.system("cls")
    input(" ______________________\n |                    |\n |                    |\n | Sistema de Locação |\n |                    |\n |____________________|\n\nRealize seu Cadastro a seguir.\nClique em qualquer tecla para continuar... ")
    os.system("cls")
    print("1º - Cadastrar Cliente")
    print("2º - Listar Clientes")
    print("3º - Cadastrar Item")
    print("4º - Listar Itens")
    print("5º - Emprestar Item")
    print("6º - Devolver Item")
    print("7º - Sair")

    try:
        escolha=int(input("--> "))
        match escolha:
            case 1:
                cadastrarocliente()
            case 2:
                listaroclientes()
            case 3:
                cadastroitem()
            case 4:
                listaritens()
            case 5:
                emprestaritem()
            case 6:
                devolveritem()
            case 7:
                print("Saindo...")
                break
            case _:

                print("Opção inválida...")
                os.system("pause")
                
    except ValueError:
        print("Digite apenas números...")
        os.system("pause")
