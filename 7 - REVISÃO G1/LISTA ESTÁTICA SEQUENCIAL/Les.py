# Tratamento de exceções:
class ListaCheiaException(Exception):
    pass

class LixtaVaziaException(Exception):
    pass

# Isso torna o código seguro e fácil de ser utillizado

# Dando início à implementação:

class Les:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho # uma lista iniciará com valores None n vezes
        self.quant = 0
    
    def inserir_fim(self, valor):
        if self.quant != self.tam_maximo:
            self.vetor[self.quant] = valor
            self.quant += 1
            return True
        return False

    def show(self):
        for i in range(self.quant): # enquanto o i for menor que o tamanho da lista.
            print(self.vetor[i], end=" ")
        print()
    
    def ver_quantidade(self):
        print(self.quant)

    def remover_fim(self):
        if self.quant != 0:
            self.quant -= 1
            return True
        return False
    
    def inserir_inicio(self, valor):
        for i in range(self.quant - 1):
            self.vetor[i] = valor
            self.quant += 1