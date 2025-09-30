import Les
l = Les.Les(5)
l.inserir_fim("A")
l.inserir_fim("B")
l.inserir_fim("C")
l.inserir_fim("D")
l.inserir_fim("E")
print("Lista com 5 valores, espera-se: A B C D E")
l.show()

print("Removendo após o 'A', espera-se: A ")
l.remover_apos("A")
l.show()
