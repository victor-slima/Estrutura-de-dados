class Les:

    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=" - ")
        print()
    
    def show_reverso(self):
        for i in range(self.quant - 1, 0 - 1, -1):
            print(self.vetor[i], end=" - ")
        print()

    def get_prim(self):
        return self.vetor[0]
    
    def get_ult(self):
        return self.vetor[self.quant - 1]
    
    def get_quant(self):
        return self.quant
    
    def get_capacidade(self):
        return self.tam
    
    def get_all_index(self):
        for i in range(self.quant):
            print(f"valor: {self.vetor[i]} - endereco: {i}")
        print()
    
    def get_index(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                return f"Valor: {self.vetor[i]} - indice: {i}"
            else:
                return -1    
    def get_valor(self, indice):
        if 0 <= indice < self.quant:
            return f"O valor na posicao {indice} é {self.vetor[indice]}"
        return False   

    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def remover(self,valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                for j in range(i, self.quant - 1):
                    self.vetor[j] = self.vetor[j + 1]
                self.quant -= 1
    
    def inserir_apos(self, valor1, valor2):
        if self.quant < self.tam:
            for i in range(self.quant):
                if self.vetor[i] == valor1:
                    for j in range(self.quant - 1, i, -1):
                        self.vetor[j + 1] = self.vetor[j]
                    self.vetor[i + 1] = valor2
                    self.quant += 1
                    return
    
    def inserir_antes(self, valor1, valor2):
        if self.quant < self.tam:
            for i in range(self.quant):
                if self.vetor[i] == valor1:
                    for j in range(self.quant - 1, i - 1, -1):
                        self.vetor[j + 1] = self.vetor[j]
                    self.vetor[i] = valor2
                    self.quant += 1
                    return
    
    def remover_anteriores(self, valor):
        # Remove todos os elementos que sao anteriores ao valor:
        for i in range(self.quant):
            if self.vetor[i] == valor:
                cont = i
                for j in range(i, self.quant):
                    self.vetor[j - cont] = self.vetor[j]
                self.quant -= cont
                return
    
    def remover_posteriores(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                cont = 0
                for j in range(i, self.quant - 1):
                    cont += 1
                self.quant -= cont
                return