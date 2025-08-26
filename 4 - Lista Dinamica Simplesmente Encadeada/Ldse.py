class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldse:
    def __init__(self): #  o nao tem tamanho definido
        # o prim e o ult recebem None
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)

        else:
            self.prim = No(valor, self.prim)
        self.quant += 1
        