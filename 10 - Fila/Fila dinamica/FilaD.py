# inserir no fim
# remover do início

class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class FilaD:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    # Mostra todos os nós da fila
    def show(self):
        aux = self.prim
        if self.quant == 0:
            print("Fila vazia.")
        else:    
            while aux is not None:
                print(aux.info, end=" ")
                aux = aux.prox
            print("\n")
    
    # Insere no final da fila
    def inserir(self, valor):
        novo = No(valor, None)
        if self.quant == 0:
            self.prim = self.ult = novo
        else:
            self.ult.prox = novo
            self.ult = novo
        self.quant += 1
    
    # Remove do início e retorna o valor removido
    def remover(self):
        if self.quant == 0:
            return None
        valor = self.prim.info
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
        return valor
    
    # Retorna o primeiro elemento (sem remover)
    def ver_primeiro(self):
        if self.prim is None:
            return None
        return self.prim.info
    
    # Verifica se a fila está vazia
    def vazia(self):
        return self.quant == 0
