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
        cont = 0
        

        # Se tiver 1 elemento ou nenhum, nao faz nada:
        if self.quant == 1 and self.quant == 0:
            print("Não é possível realizar essa operação com menos de 2 elementos na lista.")
        # Caso que há mais de dois elementos na lista:
        else:
            # Percorrendo a lista:
            aux = self.prim
            while aux != None and aux.info != valor:
                # Fazendo o aux caminhar pra frente enquanto não achar o valor.
                aux = aux.prox
            
            # Se achar o valor:
            if aux.info == valor:
                antes = aux.ant
                depois = aux.prox

                # Verificando os casos especiais:
                if antes == None:
                    aux.prox = depois.prox
                    depois.prox = aux                    



















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
