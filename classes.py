class Item:
    def __init__(self,idd,titulo):
        self.__idd=idd
        self.__titulo=titulo
        self.__disponivel = True

    def getcid(self):
        return self.__idd

    def gettitulo(self):
        return self.__titulo

    def isdisponivel(self):
        return self.__disponivel

    def alugar(self):
        if self.__disponivel:
            self.__disponivel=False
            return True
        return False

    def devolver(self):
        self.__disponivel=True
        return True

class filme(Item):
    def __init__(self,idd,titulo,genero):
        Item.__init__(self,idd,titulo)
        self.__genero=genero

    def getgenero(self):
        return self.__genero

class jogo(Item):
    def __init__(self,idd,titulo,faixa):
        Item.__init__(self,idd,titulo)
        self.__faixa=faixa

    def getFaixa(self):
        return self.__faixa

class cliente:
    def __init__(self,nome,cpf):
        self.__nome=nome
        self.__cpf=cpf
        self.__itens_alugados=[]

    def getnome(self):
        return self.__nome

    def getcpf(self):
        return self.__cpf

    def getItensalugados(self):
        return self.__itens_alugados

    def locar(self,item:Item):
        if item.alugar():
            self.__itens_alugados.append(item)
            return True
        return False

    def devolver(self,item:Item):
        if item in self.__itens_alugados:
            item.devolver()
            self.__itens_alugados.remove(item)
            return True
        return False

class locadora:
    def __init__(self,nome):
        self.__nome=nome
        self.__clientes={}
        self.__itens={}

    def cadastrarcliente(self,nome,cpf):
        self.__clientes[len(self.__clientes)+1]=cliente(nome,cpf)

    def cadastrarfilme(self,idd,titulo,genero):
        self.__itens[len(self.__itens)+1]=filme(idd,titulo,genero)

    def cadastrarJogo(self, idd,titulo,faixa):
        self.__itens[len(self.__itens)+1]=jogo(idd,titulo,faixa)

    def listarclientes(self):
        return self.__clientes

    def listaritens(self):
        return self.__itens

    def getcliente(self, cliente_id):
        return self.__clientes.get(cliente_id)

    def getitem(self, item_id):
        return self.__itens.get(item_id)