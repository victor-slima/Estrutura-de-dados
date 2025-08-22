class Les:

    # Simulação de um array em python, para compreensao de uma lista estatica sequencial.
    # criando os atributos de um array
    def __init__(self, tamanho):
        self.tam = tamanho                # Tamanho maximo da lista     
        self.vetor = [None] * tamanho     # espaço reservado para os elementos  
        self.quant = 0                    # quantidade de elementos atualmente  
        

    # Criando uma funcao que ficará responsável pela visualização dos valores.
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end="")
        print()



    # Criando uma função que insere um valor 
    def inserir_fim(self, valor):
        if self.quant == self.tam:
            print("Não há vagas")
        else:   
            self.vetor[self.quant] = valor
            self.quant += 1
    
    def remover_fim(self):
        if self.quant == 0:
            print("array vazio.")
        else:
            self.quant -= 1

    def inserir_inicio(self, valor):
        if self.quant == self.tam:
            print("Array cheio.")
        else:
            for i in range(self.quant, 0, -1):
                self.vetor[i] = self.vetor[i-1]
            self.vetor[0] = valor
            self.quant += 1
    
    