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
    def qualOrdem(self):
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
