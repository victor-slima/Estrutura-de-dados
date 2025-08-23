# Criando a classe Les, para criarmos seus atributos e criarmos metodos para manipulá-la.

class Les:

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
    
    # Criando o método que irá inserir um valor no final do vetor:
    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
    
    # Criando o método que irá remover um valor no final do vetor:
    def remover_fim(self):
        self.quant -= 1
    
    # Criando o método que irá adicionar um valor no início do vetor:
    def inserir_inicio(self, valor):
        if self.quant == self.tam:
            print("Não há espaço para mais elementos.")
        else:
            for i in range(self.quant, 0, -1):
                self.vetor[i] = self.vetor[i - 1]
            self.vetor[0] = valor
            self.quant += 1
    
    # Criando o método que irá remover um valor no início do vetor:
    def remover_inicio(self):
        # aqui, o quant é 3, e 3 - 1 aqui começa no zero, e vai até dois numeros antes do primeiro, ou seja, nao vai ate o 2 e nem o 3.
        for i in range(self.quant - 1): 
            # o i começa valendo zero, e recebe o valor 0 + 1, pois i inicia valendo zero.
            # ou seja, o valor na posicao i (que é zero, mas sera incrementado), recebera o valor da posição i + 1 (que é o índice do valor da frente).
            self.vetor[i] = self.vetor[i + 1]
         # decrementando a quantidade de elementos, pois um elemento foi removido.   
        self.quant -= 1
    
    # Criando o método que irá remover um valor que o usuário inserir:
    def remover(self, valor):
        if self.quant == 0:
            print("Array vazio.")
        else:
            for i in range(self.quant):
                if valor == self.vetor[i]:
                    print("letra removida: ", self.vetor[i])
                    # o self.quant já é 5, mas como ele está na posição de fim, ele vai até 4, e -1 ele vai até 3, 
                    # isso impede o erro de index out of range.
                    # ou seja, se o i fosse zero, iria de zero até 3. 
                    for j in range(i, self.quant - 1):
                        self.vetor[j] = self.vetor[j + 1]
                    self.quant -= 1
    
    # Criando o método que irá retornar um valor True se um valor for removido, ou False se nenhum valor for removido:
    def removerTF(self, valor):
        if self.quant == 0:
            print("Array vazio")
        else:
            for i in range(self.quant):
                if valor == self.vetor[i]:
                    # desloca todos os elementos a esquerda
                    for j in range(i, self.quant - 1):
                        self.vetor[j] = self.vetor[j + 1]
                    self.quant -= 1
                    return True  # encontrou
        return False # nao encontrou
                        
    
    # Criando o metodo que ira retornar a quantidade de valores removidos:
    def remover_contar(self, valor):
        cont = 0
        i = 0
        if self.quant == 0:
            print("Array vazio.")
        else:
            while i < self.quant:
                if valor == self.vetor[i]:
                    # Desloca os elementos pra esquerda:
                    for j in range(i, self.quant - 1):
                        self.vetor[j] = self.vetor[j + 1]
                    self.quant -= 1
                    cont += 1
                    # não incrementa o i, pois após a remoção, o próximo elemento vem para a posição atual.
                else:
                    # só se ainda não removeu, incrementa o i para ele ir pro
                    # próximo índice. 
                    i += 1 

            print(f"O valor {valor} foi removido {cont} vezes.")