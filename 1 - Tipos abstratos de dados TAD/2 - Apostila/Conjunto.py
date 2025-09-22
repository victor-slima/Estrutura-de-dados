class Conjunto:
    def __init__(self):
        self.numeros = [False] * 11
    def inserir(self, num):
        if num >= 0 and num <= 10:
            self.numeros[num] = True
        else:
            return "Valor invalido"
    def remover(self, num):
        if num >= 0 and num <= 10:
            self.numeros[num] = False
        else:
            return "Valor invalido"
    def show(self):
        for i in range(11):
            if self.numeros[i]:
                print(i)
    def uniao(self, conjunto2):
        conjunto_uniao = Conjunto()