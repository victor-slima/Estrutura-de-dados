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
            print("\n")

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
        # verificando se tem 1 só, e se o valor é o que eu escolhi.
        """
        if self.quant == 1 and self.prim.info == valor:
            self.prim = self.ult = None
            self.quant = 0
        else:
            aux = self.prim
            ant = None
            while aux.info != valor:
                ant = aux
                aux = aux.prox
            if aux.info == valor and ant == None:
                self.prim = aux.prox
                
            else:
                ant.prox = aux.prox
                self.ult = ant
            self.quant -= 1
        """
            # do fabiano:
        if self.quant == 1 and self.prim.info == valor:
            self.prim = self.ult = None
            self.quant -= 1
        else:
            aux = self.prim
            ant = None
            while aux != None and aux.info != valor:
                ant = aux
                aux = aux.prox
            
            if aux != None:
                
                if aux == self.prim:
                    self.prim = self.prim.prox
                else:
                    ant.prox = aux.prox
                  
                    if aux == self.ult:
                        self.ult = ant
                self.quant -= 1
        



    

    def removerTF(self, valor):
       
        # verificar se a lista está vazia;
        if self.quant == 0:
            return "Lista vazia", False
        
        # fazer o tratamento de somente 1 elemento na lista;
        if self.quant == 1:
            if self.prim.info == valor:
                self.prim = self.ult = None
                self.quant = 0
                return f"valor {valor} removido.", True
            else:
                return "Valor não encontrado"
        
        # fazendo os casos em que há mais de dois nós na lista:
        aux = self.prim
        ant = None
        while aux.info != valor:
            ant = aux.prox
            aux = aux.prox
        
        if aux == None:  # percorreu tudo e não achou
            return f"Valor {valor} não encontrado.", False
    
        # se remover o primeiro nó
        
        # se remover o último nó
        if aux == self.ult:
            self.ult = ant

        self.quant -= 1    
        return f"Nó com o valor {valor} removido", True
    
    # Criando o metodo removerCout:
    def removerCount(self, valor):
        cont = 0
        aux = self.prim
        ant = None
        while aux != None:
            if aux.info == valor:
                # se o valor for o primeiro nó:
                if ant == None:
                    self.prim = aux.prox
                    cont += 1
                    self.quant -= 1
                # se o valor for o último nó:    
                elif aux == self.ult:
                    self.ult = ant
                    cont += 1
                    self.quant -= 1

                # se o valor estiver no meio da lista:    
                else:
                    ant.prox = aux.prox
                
                aux = aux.prox

            else:
                ant = aux
                aux = aux.prox