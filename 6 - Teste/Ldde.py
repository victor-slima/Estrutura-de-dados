class No:
    def __init__(self, ant, info, prox):
        self.ant = ant
        self.info = info
        self.prox = prox
class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    # ---------------- inserções ----------------
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
            self.quant += 1
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1
    # --------------- remoção por intervalo ---------------
    def remover_vizinhos(self, valor):
        """
        Remove o nó anterior e o nó posterior ao nó que contém 'valor'.
        - Se 'valor' estiver no início, remove apenas o posterior.
        - Se 'valor' estiver no fim, remove apenas o anterior.
        - Se 'valor' não for encontrado, não faz nada.
        """

        aux = self.prim
        if self.quant != 0 and self.quant != 1:
            while aux != None and aux.info != valor:
                aux = aux.prox
            
            if aux != None:
                antes = aux.ant
                depois = aux.prox
            
                # se o antes existir
                if aux != self.prim:
                    if antes == self.prim:
                        self.prim = aux
                        aux.ant = None
                    else:
                        aux.ant = antes.ant
                        antes.ant.prox = aux
                    self.quant -= 1
                
                if aux != self.ult:
                    if depois == self.ult:
                        self.ult = aux
                        aux.prox = None
                    else:
                        aux.prox = depois.prox
                        depois.prox.ant = aux
                    self.quant -= 1

                                                



















    # ---------------- exibição ----------------
    def show(self):
        aux = self.prim
        while aux:
            print(aux.info, end='')
            aux = aux.prox
        print()
        


    def show_reverso(self):
        aux = self.ult
        while aux:
            print(aux.info, end='')
            aux = aux.ant
        print()
