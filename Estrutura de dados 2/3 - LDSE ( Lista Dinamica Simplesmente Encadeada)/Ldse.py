class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=" -> ")
            aux = aux.prox
        print()

    def ver_primeiro(self):
        return self.prim.info
    
    def ver_ultimo(self):
        return self.ult.info
    
    def get_quant(self):
        return f"Quantidade de elementos na lista: {self.quant}"
    
    def esta_vazia(self):
        return self.quant == 0
    
    def tamanho_atual(self):
        return self.quant
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1
    
    def remover_inicio(self):
        if self.quant > 0:
            self.prim = self.prim.prox
            self.quant -= 1
            if self.quant == 0:
                self.ult = None
    
    def inserir_fim(self, valor):
        novo = No(valor, None)
        if self.quant == 0:
            self.prim = self.ult = novo
        else:
            self.ult.prox = novo  
            self.ult = novo       
        self.quant += 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
            self.quant -= 1
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            aux.prox = None
            self.ult = aux
        self.quant -= 1
    
    def remover_irmaos(self, valor):
        if self.quant > 1:
            no_alvo = self.prim
            no_2 = None
            no_3 = None

            while no_alvo != None and no_alvo.info != valor:
                no_3 = no_2
                no_2 = no_alvo
                no_alvo = no_alvo.prox
            
            if no_alvo != None and no_alvo.info == valor:

                if no_2 != None and no_2 == self.prim:
                    self.remover_inicio()
                else:
                    if no_3 != None:
                        no_3.prox = no_alvo
                        no_2 = None
                        self.quant -= 1
                
                if no_alvo.prox != None and no_alvo.prox == self.ult:
                    self.remover_fim()
                
                else:
                    if no_alvo.prox != None:
                        no_da_frente = no_alvo.prox
                        no_alvo.prox = no_da_frente.prox
                        no_da_frente = None
                        self.quant -= 1
    
    def buscar(self, valor):
        aux = self.prim
        cont = 0
        while aux != None and aux.info != valor:
            aux = aux.prox
            cont += 1
        if aux != None and aux.info == valor:
            return f"O valor {aux.info} esta na posicao: {cont}"
        else:
            return False
    
    def remover(self, valor):
        aux = self.prim
        ant = None
        if self.quant == 1 and self.prim.info == valor:
            self.prim = self.ult = None
            self.quant -= 1
            return
        else:
            while aux != None and aux.info != valor:
                ant = aux
                aux = aux.prox
            if aux != None and aux.info == valor:
                if aux == self.prim:
                    self.remover_inicio()
                elif aux == self.ult:
                    self.remover_fim()
                else:
                    ant.prox = aux.prox
                    aux = None
                    self.quant -= 1
    
    def inserir_apos(self, valor1, valor2):
        aux = self.prim
        while aux != None and aux.info != valor2:
            aux = aux.prox
        if aux != None and aux.info == valor2:
            if aux == self.ult:
                self.inserir_fim(valor1)
            else:
                novo_no = No(valor1, aux.prox)
                aux.prox = novo_no
                self.quant += 1
    
    def inserir_antes(self, valor1, valor2):
        aux = self.prim

        if self.prim.info == valor2:
            self.inserir_inicio(valor1)
            return

        aux = self.prim
        while aux.prox != None and aux.prox.info != valor2:
            aux = aux.prox
            
        if aux.prox != None: # O próximo do aux é o alvo
            novo = No(valor1, aux.prox)
            aux.prox = novo
            self.quant += 1