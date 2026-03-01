class Conjunto:
    def __init__(self):
        self.numeros = [False] * 11

    # Metodo que mostra o conjunto:
    def show(self):
        for i in range(11):
            if self.numeros[i]:
                print(i)

    # Metodo que insere um valor em um conjunto:
    def inserir(self, numero):
        if numero >= 0 and numero <= 10:
            self.numeros[numero] = True
        else:
            return "Valor invalido"

    # Metodo que remove um valor de um conjunto:
    def remover(self, numero):
        if numero >= 0 and numero <= 10:
            self.numeros[numero] = False
        else:
            return "Valor invalido"

    def uniao(self, conjunto2):
        conjunto_uniao = Conjunto()
        for i in range(11):
            conjunto_uniao.numeros[i] = conjunto_uniao.inserir(i)

