class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def inserir(self, valor):
        if valor < self.info:
            if self.esq == None:
                print(self.info)
                self.esq = No(valor)
                #print("*")
            else:
                print(self.info)
                self.esq.inserir(valor)
                #print("+")
        else:
            if self.dir == None:
                print(self.info)
                self.dir = No(valor)
                #print("-")
            else:
                print(self.info)
                self.dir.inserir(valor)
                #print("#")
    
    # BUSCA

    def busca(self, valor):
        if valor == self.info:
            print(self.info)
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                print(self.info)
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                print(self.info)
                return self.dir.busca(valor)
    
    # IN ORDEM
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end="")
        if self.dir != None:
            self.dir.inOrdem()
    
    # PRE ORDEM
    def preOrdem(self):
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()

    # POS ORDEM
    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info,end=" ")
    
    # qual ordem
    def ordemDecrescente(self):
        if self.dir != None:
            self.dir.qualOrdem()
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.qualOrdem()
    
    # print folhas

    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq==None and self.dir == None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.printFolhas()

    # soma
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total

    # soma folhas
    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total
    
    # altura
    def altura(self):
        hesq = hdir = -1
        if self.esq != None:
            hesq = self.esq.altura()
        if slef.dir != None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)

    def busca(self, valor):
        if valor == self.info:
            return self.info
        elif valor < self.info:
            return self.esq.busca()
        else:
            return self.dir.busca()
    
    # altura do nó
    def h(self, valor):
        if valor == self.info:
            return self.altura()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.h(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)
    
    # descendente mais a direita
    def maisdir(self):
        if self.dir != None:
            return self.dir.maisdir()
        else:
            return self.info


class Tree:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.inserir(valor)
    
    # BUSCA

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
    
    # IN ORDEM

    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()

    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()
    

    # print folhas

    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    # soma
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
    
    # soma folhas

    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    # altura da arvore
    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()
    
    # altura a partir de um no
    def h(self, valor):
        if self.raiz != None:
            return self.raiz.h(valor)
    
    # descendente mais a direita
    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()


# soma dos pares
# soma dos internos (fora as folhas)
# imprimir os descendendes do no escolhido
"""
dentro de busca:
if self.esq != None:
    self.esq.inOrdem()
if self.dir != None:
    self.dir.inOrdem()

achar o 

imprimir o maior filho do no escolhido

ver se o no existe, e ver se o no tem filho, se nao tiver o direito (que é o naturalmente, o maior será o esquerdo, se houver)
e se nao tiver, nao tem filhos, ou verifica logo se o no é folha, se for folha, retorna que o nó é folha.

imprimir todos os descendentes pares de um determinado valor.

#descendente mais a direita:
dentro do primeiro if de busca(self, valor):
    if self.dir != None:
        return self.dir.info
    elif self.esq != None:
        return self.esq.info

# Quantidade de nos até o no mais a direita
def maisdir(self):
    if self.dir != None:
        return self.dir.maisdir() + 1
    else:
        return 

# quantidade de ancestrais agora:
def maisdir(self):
    if self.dir != None:
        return self.dir.maisdir() + self.info
    else:
        return self.info

# mostrar todos
def maisdir(self):
    if self.dir != None:
        print(self.dir.maisdir())
    else:
        print(self.info)

# mostrar somente os ancestrais

"""