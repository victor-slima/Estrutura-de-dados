class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
    
class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end="")
            aux = aux.prox
        print("\n")
    
    def show_reverso(self):
        aux = self.ult
        while aux != None:
            print(aux.info, end="")
            aux = aux.ant
        print("\n")

    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            # o anterior do antigo primeiro tem que apontar primeiro para o novo primeiro: 
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1
    
    # inserindo o remover_inicio(self, valor):
    def remover_inicio(self, valor):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1
    
    # inserindo o remover_fim(self, valor):
    def remover_fim(self, valor):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ut.prox = None
        self.quant -= 1
    
    # inserindo ver primeiro:
    def ver_primeiro(self):
        print(self.prim.info)
    
    # inserindo o ver ultimo:
    def ver_ultimo(self):
        print(self.ult.info)
    
    # inserindo o ver quantidade:
    def ver_quantidade(self):
        print(self.quant)
    
    # inserindo o esta_vazia:
    def esta_vazia(self):
        return self.quant == 0

    # inserindo o método remover:
    def remover(self, valor):
        aux = self.prim
        while aux != None and aux.info != valor:
            aux = aux.prox
        if aux == None:
            print("Valor não encontrado.")
        
        if aux.ant == None: # é o primeiro elemento
            aux = aux.prox
            self.prim = aux
        elif aux.prox == None:
            aux = self.ult = aux.ant
            self.ult.prox = None
        else:
            aux.ant.prox = aux.prox
            aux.prox.ant = aux.ant
        self.quant -= 1

    # Inserindo o removerTF: retorna True se removeu um valor, e false se não removeu.
    def removerTF(self, valor):
        aux = self.prim
        if self.quant == 1 and aux.info == valor:
            self.prim = self.ult = None
            self.quant -= 1

            return True
       
        while aux != None and aux.info != valor:
            aux = aux.prox
        if aux == None:
            print("Valor não está na lista.")
            return print(False)
        if aux.ant == None:
            aux = self.prim = aux.prox
            self.prim.ant = None    
        elif aux.prox == None:
            aux = self.ult = aux.ant
            self.ult.prox = None
        else:
            aux.ant.prox = aux.prox
            aux.prox.ant = aux.ant
    
        self.quant -= 1
        print(f"Valor '{valor}' removido. ")                
        return print(True)