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
            print(aux.info, end=" ")
            aux = aux.ant
        print("")

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
    
    # inserindo o remover_inicio(self):
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1
    
    # inserindo o remover_fim(self):
    def remover_fim(self):
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
            return 
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
            return False
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
        return True
    
    # Inserindo o metodo remover_contar:
    
    def remover_contar(self, valor):
        cont = 0
        aux = self.prim

        while aux is not None:
            proximo = aux.prox  # salva o próximo antes de remover aux

            if aux.info == valor:
                if aux == self.prim and aux == self.ult:
                    # único elemento na lista
                    self.prim = self.ult = None
                
                # Valor sendo o primeiro da lista:
                elif aux == self.prim:
                    self.prim = aux.prox
                    self.prim.ant = None
                
                # Valor sendo o último da lista:
                elif aux == self.ult:
                    self.ult = aux.ant
                    self.ult.prox = None
                
                # Valor estando no meio da lista:
                else:
                    aux.ant.prox = aux.prox
                    aux.prox.ant = aux.ant

                cont += 1
                self.quant -= 1

            aux = proximo  # vai para o próximo nó

        print(f"O valor {valor} foi removido {cont} vezes")
    
    def remover_vizinhos(self, valor):
        """
        Remove o nó anterior e o nó posterior ao nó que contém 'valor'.
        - Se 'valor' estiver no início, remove apenas o posterior.
        - Se 'valor' estiver no fim, remove apenas o anterior.
        - Se 'valor' não for encontrado, não faz nada.
        """
        aux = self.prim
        if self.quant <= 1:
            print("Não tem o que fazer aqui não chapa.")
        else:
            while aux != None and aux.info != valor:
                aux = aux.prox

            if aux != None:
                antes = aux.ant
                depois = aux.prox
                    # se for o primeiro
                if aux == self.prim and depois:
                    self.prim.prox = depois.prox
                    if depois.prox:   # garante que não é None
                        depois.prox.ant = aux
                    else:
                        self.ult = aux
                        aux.prox = None
                    self.quant -= 1

                # se for o último
                elif aux == self.ult and antes:
                    self.ult.ant = antes.ant
                    if antes.ant:     # garante que não é None
                        antes.ant.prox = aux
                    else:
                        self.prim = aux
                        aux.ant = None
                    self.quant -= 1

                # se o vizinho esquerdo for o primeiro
                elif antes == self.prim and depois:
                    self.prim = aux
                    aux.ant = None
                    self.prim.prox = depois.prox
                    if depois.prox:   # pode ser None
                        depois.prox.ant = self.prim
                    else:
                        self.ult = aux
                        aux.prox = None
                    self.quant -= 2

                # se o vizinho direito for o último
                elif depois == self.ult and antes:
                    self.ult = aux
                    aux.prox = None
                    self.ult.ant = antes.ant
                    if antes.ant:     # pode ser None
                        antes.ant.prox = self.ult
                    else:
                        self.prim = aux
                        aux.ant = None
                    self.quant -= 2

                # caso geral (meio da lista)
                else:
                    antes.ant.prox = aux
                    depois.prox.ant = aux
                    aux.prox = depois.prox
                    aux.ant = antes.ant
                    self.quant -= 2
            else:
                print("Valor não está na lista.")