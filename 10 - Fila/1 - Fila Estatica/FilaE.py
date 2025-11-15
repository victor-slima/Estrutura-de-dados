class Fila_estatica:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0
    
    def inserir(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
    
    def remover(self):
        for i in range(1, self.quant):
            self.vetor[i -1] = self.vetor[i]
        self.quant -= 1
    
    def esta_vazia(self):
        if self.quant == 0:
            return "Lista vazia"
    
    def esta_cheia(self):
        if self.quant == self.tam:
            return "Lista cheia"
        
    def ver_primeiro(self):
        return self.vetor[0]
    
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i])
        print()

    def tamanho_atual(self):
        return self.quant

    def capacidade(self):
        return self.tam