class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Lee:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * self.tam_maximo
        self.quant = 0

        self.prox_pos_vazia = self.inicializa_estrutura()

        self.prim = -1
        self.ult = -1
    
    def inicializa_estrutura(self):
        for i in range(self.tam_maximo - 1):
            self.vetor[i] = No(None, i+1)
        self.vetor[self.tam_maximo - 1] = No(None, i + 1)
        return 0
    