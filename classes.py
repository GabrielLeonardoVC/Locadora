class item:
    def __init__(self,idd,titulo):
        self.__idd=idd
        self.__titulo=titulo
        self.__disponivel=True

    def getcodigo(self):
        return self.__idd
    def gettitulo(self):
        return self.__titulo
    def getdisponivel(self):
        return self.__disponivel
    
    def alugar(self):
        if self.__disponivel:
            self.__disponivel=False
            return True
        return False
    
    def devolver(self):
        self.__disponivel=True
        return True
    
class filme(item):
    def __init__(self, idd, titulo, genero):
        self.__idd=idd
        self.__genero=genero
        self.__titulo=titulo
        self.__item__disponivel=True

        def genero(self):
            return self.__genero
        
class jogos(item):
    def __init__(self,idd,titulo,genero):
        self.__idd=idd
        self.__titulo=titulo
        self.__genero=genero
        self.__item__disponivel= True

    def getgenero(self):
         return self.__genero

class clientes:
    def __init__(self, nome, cpf):
        self.__nome=nome
        self.__cpf=cpf
        self.__itemalugado=[]

def getnome(self):
    return self.__nome

def getcpf(self):
    return self.__cpf

def itemalugado(self):
    return self.__itemalugado

def locacao(self,item:item):
    if item.disponivel():
        item.alugado()
        self.__item.disponivel.append(item)
        return True
    return False


def devolver(self, item:item):
    if item in self.__itemalugado:
        item.devolver()
        self.__itemalugado.remove(item)
        return True
    return False

def listaritem(self):
    return self.__itemalugado


class locadora:
    def __init__(self, nome):
        self.__nome=nome
        self.__clientes={}
        self.__item={}


def getclientes(self):
    return self.__clientes

def getitem(self):
    return self.__item



def cadastrarocliente(self,nome,cpf):
        self.__clientes[len(self.__clientes)+1]=clientes(nome,cpf)
    
def cadastrarofilme(self,idd, titulo, genero):
        self.__item[len(self.__item)+1]=filme(idd,titulo,genero)
    
def cadastrarojogo(self,idd,titulo,genero):
        self.__item[len(self.__item)+1] = jogos(idd,titulo,genero)
    

 
def listarclientes(self):
        return self.__clientes
    

def listarItens(self):
        return self.__item