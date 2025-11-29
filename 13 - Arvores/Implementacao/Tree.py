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