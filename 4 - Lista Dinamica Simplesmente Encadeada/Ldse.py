class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
    
class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    # Criando o metodo show()
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=" ")
            aux = aux.prox


    # Criando o método inserir_inicio:
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1