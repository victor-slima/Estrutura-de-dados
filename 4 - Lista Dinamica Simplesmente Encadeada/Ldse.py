class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
    
class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    # Criando o metodo show()
    def show(self):
        aux = self.prim
        if self.quant == 0:
            print("Lista sem nenhum nó.")
        else:    
            while aux != None:
                print(aux.info, end=" ")
                aux = aux.prox

    # Criando o ver primeiro:
    def ver_primeiro(self):
        if self.prim == None:
            return None
        return self.prim.info
    
    def ver_ultimo(self):
        if self.ult == None:
            return None
        return self.ult.info


    # Criando o método inserir_inicio:
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1
    
    # Criando o método inserir fim:
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1

    # Criando o remover inicio:
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
    
    # Criando o remover fim:
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            self.ult = aux
            self.ult.prox = None
        self.quant -= 1

    def remover(self, valor):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            ant = None
            while aux.info != valor:
                ant = aux
                aux = aux.prox
            ant.prox = aux.prox

            print(ant.info)
            print(aux.info)
        
        self.quant -= 1