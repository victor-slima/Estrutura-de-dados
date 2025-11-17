class No:
    def __init__(self, valor, prioridade, proximo):
        self.info = valor
        self.prioridade = prioridade
        self.prox = proximo

class Fila_prioridade:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir(self, valor, prioridade):
        if self.quant == 0:
            self.prim = self.ult = No(valor, prioridade, None)
        else:
            self.ult.prox = self.ult = No(valor, prioridade, None)
        self.quant -= 1
    
    def remover(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = maior = self.prim
            maior_prioridade = self.prim.prioridade
            ant = None
            while aux is not None:
                if aux.prioridade > maior_prioridade:
                    maior_prioridade = aux.prioridade
                    print(aux.info, maior_prioridade)
                    maior = aux
                    ant_maior = ant
                ant = aux
                aux = aux.prox
            if maior == self.prim:
                self.prim = self.prim.prox
            else:
                ant_maior.prox = maior.prox
                if maior == self.ult:
                    self.ult = ant_maior
                    self.ult.prox = None
        self.quant -= 1
    
    def esta_vazia(self):
        return self.quant == 0
    
    def tamanho_atual(self):
        return self.quant
    
    def ver_primeiro(self):
        return self.prim.info
    
    def show(self):
        aux = self.prim
        while aux is not None:
            print("Valor: ", aux.info, " - Prioridade: ", aux.prioridade)
            aux = aux.prox
        print()