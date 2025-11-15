class Fila_circular:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.quant = 0
    
    # Calcula a posicao do proximo elemento do vetor, sendo um tipo de apontamento.
    def calcularPosicao(x, y):
        return x % y
    
    def inserir(self, valor):
        self.vetor[self.fim] = valor
        self.fim = self.calcularPosicao((self.fim + 1), self.tam)
    
    def remover(self):
        self.inicio = self.calcularPosicao((self.inicio + 1) % self.tam_maximo)
        self.quant -= 1
    
    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam_maximo
    
    def show(self):
        for i in range(self.quant):
            print(self.vetor[(self.inicio + i) % self.tam_maximo], end=' ')
        print()

    def ver_primeiro_elemento(self):
        return self.vetor[self.inicio]