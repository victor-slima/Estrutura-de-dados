class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class PilhaD:
    def __init__(self):
        self.topo = None
        self.quant = 0
    # o push é o inserir inicio
    def push(self, valor):
        self.topo = No(valor, self.topo)
        self.quant += 1
    
    # o pop é o remover inicio
    def pop(self):
        if self.topo is None:
            return None
        valor = self.topo.info
        self.topo = self.topo.prox
        self.quant -= 1
        return valor

    
    # Ver topo é o ver ultimo:
    def verTopo(self):
        if self.topo == None:
            return "Não há valores na pilha"
        else:
            return self.topo.info
    
    # vendo se está vazia:
    def vazia(self):
        return self.quant == 0
    
    # mostrando a pilha:
    def show(self):
        aux = self.topo
        while aux != None:
            print(aux.info, end=" ")
            aux = aux.prox
        print()