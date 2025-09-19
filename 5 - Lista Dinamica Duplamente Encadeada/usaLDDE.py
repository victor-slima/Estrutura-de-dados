import Ldde

l = Ldde.Ldde()
"""
l.inserir_inicio("C")
l.inserir_inicio("B")
l.inserir_inicio("A")
l.show()
l.show_reverso()

l.ver_primeiro()
l.ver_ultimo()
l.ver_quantidade()
l.esta_vazia()
"""

l.inserir_fim("A")
l.inserir_fim("B")
l.inserir_fim("C")
l.inserir_fim("D")
l.inserir_fim("E")
print("Lista: A B C D E")
print("Removendo o A")
l.remover("A")
l.show()
print("\n")

print("Removendo o C")
l.remover("C")
l.show()
print("\n")

print("Removendo o E")
l.remover("E")
l.show()
print("\n")

print("Vendo o primeiro: espera-se => B")
l.ver_primeiro()
print("\n")

print("Vendo o ultimo: espera-se => D ")
l.ver_ultimo()
print("\n")

l.show()