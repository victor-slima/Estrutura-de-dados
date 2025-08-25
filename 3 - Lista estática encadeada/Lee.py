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
    
    def remover_irmaos(self, valor):
        if self.quant != 1 and self.quant != 0:
            anterior_do_anterior = -1
            anterior = -1
            atual = self.prim
            while atual != -1 and self.vetor[atual].info != valor:
                anterior_do_anterior = anterior
                anterior = atual
                atual = self.vetor[atual].prox
            if atual != -1 and self.vetor[atual].info == valor:
                if self.vetor[self.prim].prox == atual:
                    self.remover_inicio()
                else:
                    if atual != self.prim:
                        self.vetor[anterior_do_anterior].prox = atual
                        self.devolve_no(anterior)
                        self.quant -= 1
                if self.vetor[atual].prox == self.ult:
                    self.remover_fim()
                else:
                    if atual != self.ult:
                        proximo = self.vetor[atual].prox
                        self.vetor[atual].prox = self.vetor[proximo].prox
                        self.devolve_no(proximo)
                        self.quant -= 1
    def remover_elemento(self, valor):
        if self.esta_vazia():
            print("Lista vazia!")
            return False

        ant = -1
        atual = self.prim

        # procurar o nó com o valor
        while atual != -1 and self.vetor[atual].info != valor:
            ant = atual
            atual = self.vetor[atual].prox

        if atual == -1:
            return False  # não encontrou

        # remover do início
        if ant == -1:
            self.prim = self.vetor[atual].prox
            if self.prim == -1:  # se ficou vazio
                self.ult = -1
        else:
            self.vetor[ant].prox = self.vetor[atual].prox
            if atual == self.ult:  # se removeu o último
                self.ult = ant

        # devolve o nó
        self.devolve_no(atual)
        self.quant -= 1
        return True

    def buscar(self, valor):
        atual = self.prim
        pos = 0
        while atual != -1:
            if self.vetor[atual].info == valor:
                return pos
            atual = self.vetor[atual].prox
            pos += 1
        return None

    def inserir_apos(self, valor1, valor2):
        if self.esta_cheia():
            print("Lista cheia!")
            return False

        # procurar valor2
        atual = self.prim
        while atual != -1 and self.vetor[atual].info != valor2:
            atual = self.vetor[atual].prox

        if atual == -1:
            return False  # não encontrou valor2

        # pega nó livre
        novo = self.prox_pos_vazia
        self.prox_pos_vazia = self.vetor[novo].prox

        self.vetor[novo].info = valor1
        self.vetor[novo].prox = self.vetor[atual].prox
        self.vetor[atual].prox = novo

        if atual == self.ult:  # se inseriu no fim
            self.ult = novo

        self.quant += 1
        return True

    def inserir_antes(self, valor1, valor2):
        if self.esta_cheia():
            print("Lista cheia!")
            return False

        # caso especial: valor2 é o primeiro
        if self.prim != -1 and self.vetor[self.prim].info == valor2:
            self.inserir_inicio(valor1)
            return True

        ant = -1
        atual = self.prim
        while atual != -1 and self.vetor[atual].info != valor2:
            ant = atual
            atual = self.vetor[atual].prox

        if atual == -1:
            return False  # valor2 não encontrado

        # pega nó livre
        novo = self.prox_pos_vazia
        self.prox_pos_vazia = self.vetor[novo].prox

        self.vetor[novo].info = valor1
        self.vetor[novo].prox = atual
        self.vetor[ant].prox = novo

        self.quant += 1
        return True
