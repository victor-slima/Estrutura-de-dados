class FilaE:

    # Criando o método que irá inicializar a construção de outros métodos utilizando os atributos, que serao criados Neste método:        
    def __init__(self, tamanho):                                    
        self.tam = tamanho              # criando o primeiro atributo self.tam, que receberá tamanho.
        self.vetor = [None] * tamanho   # criando o segundo atributo self.vetor, que receberá x vezes tamanho.
        self.quant = 0                  # criando o terceiro atributo self.quant, que será a quantidade de valores incluidos no vetor.
    
    # Criando o metodo que irá mostrar os elementos que estarão dentro do vetor:
    def show(self):
        # O "i" irá iterar pela quantidade de elementos inseridos no vetor, e não pelo tamanho.
        for i in range(self.quant):
            print(self.vetor[i], end="|")
        if self.quant == 0:
            print("Array vazio.")
        print()

    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
    
    def remover_inicio(self):
        # aqui, o quant é 3, e 3 - 1 aqui começa no zero, e vai até dois numeros antes do primeiro, ou seja, nao vai ate o 2 e nem o 3.
        for i in range(self.quant - 1): 
            # o i começa valendo zero, e recebe o valor 0 + 1, pois i inicia valendo zero.
            # ou seja, o valor na posicao i (que é zero, mas sera incrementado), recebera o valor da posição i + 1 (que é o índice do valor da frente).
            self.vetor[i] = self.vetor[i + 1]
         # decrementando a quantidade de elementos, pois um elemento foi removido.   
        self.quant -= 1
    
    def ver_primeiro(self):
        return self.vetor[0]