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

class Tree:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.inserir(valor)
