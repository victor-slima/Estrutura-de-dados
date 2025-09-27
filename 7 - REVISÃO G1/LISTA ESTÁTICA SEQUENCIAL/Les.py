# Dando início à implementação:

class Les:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho # uma lista iniciará com valores None n vezes
        self.quant = 0
    
    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor # o vetor receberá o valor no índice, que é self.quant.
        self.quant += 1 # quant vai receber +1, assim, a próxima posição (se existir), estará livre.

    def show(self):
        for i in range(self.quant): # enquanto o i for menor que o tamanho da lista.
            print(self.vetor[i], end=" ")
        print()
    
    def ver_quantidade(self):
        print(self.quant)

    def remover_fim(self):
        self.quant -= 1