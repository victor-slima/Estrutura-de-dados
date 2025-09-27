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
