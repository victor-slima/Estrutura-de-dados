class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
    
class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            # o anterior do antigo primeiro tem que apontar primeiro para o novo primeiro: 
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1
    
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end="")
            aux = aux.prox
        print("\n")