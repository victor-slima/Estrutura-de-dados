class No:
    def __init__(self, anterior, valor, proximo):
        self.info = valor
        self.prox = proximo

class Lddec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info)
            aux = aux.prox
    
    def ver_quantidade(self):
        return print(f"Quantidade de elementos na lista: {self.quant}")
    
    def ver_primeiro(self):
        return print(f"O primeiro elemento da lista: {self.prim.info}")
    
    def ver_ultimo(self):
        return print(f"O ultimo elemento da lista: {self.ult.info}")
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
            self.prim.ant = self.ult.prox = self.prim
        else:
            self.prim.ant = self.prim = No(self.ult, valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
            self.prim.ant = self.ult.prox = self.prim
        else:
            self.ult.prox = self.ult = No(self.ult, valor, self.prim)
            self.prim.ant = self.ult
        self.quant += 1
    
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = self.ult
            self.ult.prox = self.prim
        self.quant -= 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = self.prim
            self.prim.ant = self.ult
        self.quant -= 1
    
    def remover_todos_apos(self, valor):
        # Remover todos apos o valor selecionado;
        if self.quant == 1:
            print("nao ha valores apos o valor selecionado.")
        else:
            aux = self.prim
            cont = 1
            while aux.info != valor:
                aux = aux.prox
                cont += 1
            if aux.info == valor:
                self.ult = aux
                self.ult.prox = self.prim
                self.prim.ant = self.ult
            elif aux == self.ult:
                print("Nao ha valores apos o valor pois é o ultimo")
        self.quant = cont
    
    def remover_todos_antes(self, valor):
        aux = self.prim
        if self.quant == 1:
            print("nao ha valores apos o valor selecionado.")
        else:
            cont = 1
            while aux.info != valor:
                aux = aux.prox
                cont += 1
            if aux.info == valor:
                # O valor pode ser o ultimo:
                if aux == self.ult:
                    self.prim = aux
                    self.prim.ant = self.ult.prox = aux
                    self.quant = 1
                    return
                
                # o valor pode ser o primeiro:
                elif aux == self.prim:
                    print("Nao ha nenhum valor a remover pois o valor selecionado e o primeiro.")
                
                # valor esta no meio:
                else:
                    self.prim = aux
                    self.prim.ant = self.ult
                    self.ult.prox = self.prim
            self.quant -= cont
