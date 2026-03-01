import TAD

# Criacao dos objetos da classe Conjunto
conjunto1 = TAD.Conjunto()
conjunto2 = TAD.Conjunto()

print("Inserindo valores nos conjuntos 1 e 2.")
conjunto1.inserir(5)
conjunto1.inserir(7)
conjunto1.inserir(8)
conjunto2.inserir(5)
conjunto2.inserir(9)
conjunto2.inserir(0)
conjunto1.show()
conjunto2.show()

print("Removendo valores nos conjuntos 1 e 2.")
conjunto1.remover(5)
conjunto1.remover(7)
conjunto1.remover(8)
