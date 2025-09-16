import os
from classes import *
locadoraa=locadora("Locadora")

def pause():
    os.system("pause")

def cadastrarocliente():
    nome=input("Digite seu nome: ")
    os.system("cls")
    cpf = input("Digite seu CPF: ")
    os.system("cls")
    locadoraa.cadastrarcliente(nome,cpf)
    print("Cadastro Concluído")
    pause()

def cadastroitem():
    while True:
        print("1ºFilme\n2ºJogo\n3ºVoltar")
        tipo=int(input("Digite o que deseja fazer à seguir\n--> "))
        os.system("cls")

        if tipo==1:
            idd=int(input("Digite o Id do filme: "))
            os.system("cls")
            titulo=input("Título do filme: ")
            os.system("cls")
            genero=input("Gênero: ")
            os.system("cls")
            locadoraa.cadastrarfilme(idd,titulo,genero)
            print("Filme cadastrado com sucesso!")
            pause()
            break

        elif tipo==2:
            idd=int(input("Digite o Id do jogo: "))
            os.system("cls")
            titulo=input("Digite o nome do jogo: ")
            os.system("cls")
            faixa=input("Digite a faixa etária\n(Livre | 12 | 14 | 16 | 18 |)\n--> ")
            os.system("cls")
            locadoraa.cadastrarJogo(idd,titulo,faixa)
            print("Jogo cadastrado com sucesso!")
            pause()
            break

        elif tipo == 3:
            break

        else:
            print("Opção inválida...")
            pause()

def listaroclientes():
    clientes=locadoraa.listarclientes()
    if not clientes:
        print("Nenhum cliente cadastrado...")
    else:
        for numero,cliente in clientes.items():
            print(f"{numero}-{cliente.getnome()} | CPF: {cliente.getcpf()}")
    pause()

def listaritens():
    itens=locadoraa.listaritens()
    if not itens:
        print("Nenhum item foi cadastrado...")
    else:
        for iid,item in itens.items():
            status="Disponível" if item.isdisponivel() else "Alugado"
            print(f"{iid}-{item.gettitulo()} ({status})")
    pause()

def emprestaritem():
    listaroclientes()
    cliente_id=int(input("Digite o Id do cliente: "))
    os.system("cls")
    cliente=locadoraa.getcliente(cliente_id)
    if not cliente:
        print("O cliente não foi encontrado...")
        pause()
        return

    listaritens()
    item_id=int(input("Digite o Id do item: "))
    item=locadoraa.getitem(item_id)
    if not item:
        print("O item não foi encontrado...")
        pause()
        return

    if cliente.locar(item):
        print("O item foi emprestado com sucesso!")
    else:
        print("O item está indisponível para empréstimo no momento...")
    pause()

def devolveritem():
    listaroclientes()
    cliente_id=int(input("Digite o Id do cliente: "))
    os.system("cls")
    cliente=locadoraa.getcliente(cliente_id)
    if not cliente:
        print("O cliente não foi encontrado...")
        pause()
        return

    itens=cliente.getItensalugados()
    if not itens:
        print("Esse cliente não possui nenhum item alugado.")
        pause()
        return

    for num, item in enumerate(itens,1):
        print(f"{num}-{item.gettitulo()}")

    escolha=int(input("Escolha o número do item para devolver: "))
    if 1<=escolha<=len(itens):
        item=itens[escolha-1]
        cliente.devolver(item)
        print("O item foi devolvido com sucesso!")
    else:
        print("Escolha inválida...")
    pause()
