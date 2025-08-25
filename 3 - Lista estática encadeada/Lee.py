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
    
    def ocupa_no(self, valor, proximo):
        posicao_livre = self.prox_pos_vazia
        self.prox_pos_vazia = self.vetor[self.prox_pos_vazia].prox
        self.vetor[posicao_livre] = No(valor, proximo)
        return posicao_livre
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor, - 1)
            self.quant += 1
        else:
            self.prim = self.ocupa_no(valor, self.prim)
            self.quant += 1
    
    # Implementando o remover_inicio:
    def remover_inicio(self):
        if self.quant == 1:
            self.devolve_no(self.prim)
            self.prim = self.ult
        else:
            novo_prim = self.vetor[self.prim].prox
            self.devolve_no(self.prim)
            self.prim = novo_prim
        self.quant -= 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor, -1)
            self.quant += 1
        else:
            self.vetor[self.ult].prox = self.ult = self.ocupa_no(valor, -1)
            self.quant += 1

    def show(self):
        aux = self.prim
        while aux != -1:
            print(self.vetor[aux].info, end="")
            aux = self.vetor[aux].prox
    
    def show_vetor(self):
        print('Prim = ', self.prim)
        print('Ult = ', self.ult)
        print('Primeira posicao vazia = ', self.prox_pos_vazia)
        print('Vetor = ')
        for i in range(self.tam_maximo):
            print(i, self.vetor[i].info, self.vetor[i].prox)
    
    # Implementando o método devolve_no:
    def devolve_no(self, no):
        self.vetor[no].prox = self.prox_pos_vazia
        self.prox_pos_vazia = no
    
    
    def remover_fim(self):
        if self.quant == 1: 
            self.devolve_no(self.prim)
            self.prim = self.ult = -1
        else: 
            aux = self.prim
            while self.vetor[aux].prox != self.ult:
                aux = self.vetor[aux].prox
            self.devolve_no(self.ult)  
            self.vetor[aux].prox = -1
            self.ult = aux
        self.quant -= 1
       
    def tamanho_atual(self):
        return self.quant  
    
    def capacidade(self):
        return self.tam_maximo  
     
    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam_maximo

 
    def ver_primeiro(self):
        if self.prim != -1:
            return self.vetor[self.prim].info
        return None  

    def ver_ultimo(self):
        if self.ult != -1:
            return self.vetor[self.ult].info
        return None 
    
    
