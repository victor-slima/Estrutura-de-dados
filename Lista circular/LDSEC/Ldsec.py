class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldsec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info)
            aux = aux.prox

    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.ult.prox = self.prim
        else:
            self.prim = self.ult.prox = No(valor, self.prim)
        self.quant += 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.ult.prox = self.prim
        else:
            self.ult.prox = self.ult = No(valor, self.prim)
        self.quant += 1
    
    def remover_inicio(self, valor):
        if self.quant == 1:
            self.prim = self.ult == None
        else:
            self.prim = self.ult.prox = self.prim.prox
        self.quant -= 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult == None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            self.ult = aux
            self.ult.prox = self.prim
        self.quant -= 1