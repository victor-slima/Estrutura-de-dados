class pilha_estatica:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0
    
    def push(self, valor):
        self.quant += 1
        self.vetor[self.quant] = valor
    
    def pop(self):
        if not self.esta_vazia():
            self.quant -= 1
    
    def esta_vazia(self):
        return self.quant == -1

    def esta_cheia(self):
        return self.quant == self.tam_maximo - 1

    def ver_quant(self):
        return self.vetor[self.quant]
    
    def ver_topo(self):
        return self.vetor[self.quant - 1]

    def show(self):
        for i in range(self.quant + 1):
            print(self.vetor[i], end=' ')
        print()
    
    def tamanho_atual(self):
        return self.quant + 1

    def capacidade(self):
        return self.tam_maximo