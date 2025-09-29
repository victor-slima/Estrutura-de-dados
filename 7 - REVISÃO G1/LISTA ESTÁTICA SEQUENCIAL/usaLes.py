import Les

""" # 1
l = Les.Les(15)

l.inserir_fim("A")
l.inserir_fim("B")
l.inserir_fim("C")
l.inserir_fim("D")
l.inserir_fim("E")
l.inserir_fim("F")
l.inserir_fim("G")
l.inserir_fim("H")
l.inserir_fim("I")
l.inserir_fim("J")
l.inserir_fim("K")
l.inserir_fim("L")
l.inserir_fim("M")
l.inserir_fim("N")
l.inserir_fim("O")
print()

print("Lista completa, saída esperada: \nA B C D E F G H I J K L M N O")
l.show()
print()

print("Quantidade de elementos na lista, saída esperada: \n15")
l.ver_quantidade()
print()

print("Removendo o último valor, saída esperada: \nA B C D E F G H I J K L M N")
l.remover_fim()
l.show()
l.ver_quantidade()
"""
l = Les.Les(5)
l.inserir_fim(1)
l.inserir_fim(2)
l.inserir_fim(3)
l.inserir_fim(4)
l.inserir_fim(5)
l.show()

l.buscar(3)

l.remover_irmaos(3)
l.show()