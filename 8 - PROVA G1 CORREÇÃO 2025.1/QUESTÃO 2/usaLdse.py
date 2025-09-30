import Ldse

l = Ldse.Ldse()
"""
l.inserir_inicio("B")
l.inserir_inicio("A")
l.inserir_inicio("C")

print("INSERINDO INICIO, B A C, SAÍDA ESPERADA: C A B.")
l.show()
print()

l.inserir_fim("I")
l.inserir_fim("D")
l.inserir_fim("E")
print("INSERINDO FIM, I D E, SAÍDA ESPERADA: C A B I D E.")
l.show()
print()

l.remover_inicio()
print("REMOVENDO O PRIMEIRO NÓ DA LISTA")
l.show()
print()

print("VENDO O PRIMEIRO DA LISTA:")
print(l.ver_primeiro())
print()

print("VENDO O ÚLTIMO DA LISTA:")
print(l.ver_ultimo())
print()

l.remover_fim()
print()
print("atual ultimo da lista")
print(l.ver_ultimo())

print("printando a lista atual: saída esperada => A B I D")
l.show()
print()

l.inserir_fim("J")
l.show()
print()

print("removendo um único valor da lista: ")
l.remover("I")
l.show()
print()

print("Removendo todos os valores da lista. Saída esperada: Lista sem nenhum nó.")
l.remover("A")
l.remover("B")
l.remover("D")
l.remover("J")
l.show()
print()
"""
"""
print("Inserindo valores na lista, saída esperada: A B C D E F")
l.inserir_fim("A")
l.inserir_fim("B")
l.inserir_fim("A")
l.inserir_fim("D")
l.inserir_fim("A")
l.inserir_fim("F")
l.show()
print()

print("Removendo o valor 'A', saída esperada: True ")
l.removerTF("A")
l.show()

print("Testando o remover contar, saida esperada: B D F.")
l.removerCount("A")
l.ver_primeiro()
l.ver_ultimo()
l.show()

l.inserir_fim("C")
l.inserir_inicio("B")
l.inserir_inicio("A")
l.show()

l.remover("C")
l.show()

l.inserir_fim("D")
l.show()

l.remover("A")
l.show()

l.inserir_inicio("E")
l.show()

l.remover("B")
l.show()

l.show_reverso()
"""

l.inserir_fim("A")
l.inserir_fim("B")
l.inserir_fim("C")
l.inserir_fim("D")
l.inserir_fim("E")
l.show()

print("Removendo todos os elementos apos o valor B, espera-se: A B")
l.remover_todos_apos("B")
l.show()
l.ver_ultimo()
l.ver_quantidade()