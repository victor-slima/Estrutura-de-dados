import FilaD

class FilaP:
    def __init__(self):
        self.f1 = FilaD.FilaD()
        self.f2 = FilaD.FilaD()
        self.f3 = FilaD.FilaD()
        self.f4 = FilaD.FilaD()
        self.quant = 0
    
    # Insere um valor na fila de acordo com a prioridade
    def inserir(self, valor, prioridade):
        if prioridade == 1:
            self.f1.inserir(valor)
        elif prioridade == 2:
            self.f2.inserir(valor)
        elif prioridade == 3:
            self.f3.inserir(valor)
        elif prioridade == 4:
            self.f4.inserir(valor)
        else:
            print("Prioridade inválida!")
            return
    
    # Remove da fila de maior prioridade (1 -> 4)
    def remover(self):
        if not self.f1.vazia():
            return self.f1.remover()
        elif not self.f2.vazia():
            return self.f2.remover()
        elif not self.f3.vazia():
            return self.f3.remover()
        elif not self.f4.vazia():
            return self.f4.remover()
        else:
            return None  # Todas vazias
    
    # Retorna o primeiro elemento (sem remover)
    def ver_primeiro(self):
        if not self.f1.vazia():
            return self.f1.ver_primeiro()
        elif not self.f2.vazia():
            return self.f2.ver_primeiro()
        elif not self.f3.vazia():
            return self.f3.ver_primeiro()
        elif not self.f4.vazia():
            return self.f4.ver_primeiro()
        else:
            return None
    
    # Verifica se a fila está vazia
    def vazia(self):
        return self.quant == 0
    
    # Exibe todas as filas de prioridade
    def show(self):
        print("Fila de prioridade:")
        print("Prioridade 1 (Imediato):")
        self.f1.show()
        print("Prioridade 2 (Grave):")
        self.f2.show()
        print("Prioridade 3 (Médio):")
        self.f3.show()
        print("Prioridade 4 (Normal):")
        self.f4.show()
