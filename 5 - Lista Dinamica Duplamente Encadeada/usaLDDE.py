import Ldde

l = Ldde.Ldde()

print("Inserindo valores na lista: A B C D E")
l.inserir_inicio("C")
l.inserir_inicio("B")
l.inserir_inicio("A")
l.inserir_fim("D")
l.inserir_fim("E")
print("")


print("Mostrando a lista:")
l.show()
print("")

print("Mostrando a lista em ordem reversa:")
l.show_reverso()
print("")

print("Vendo o primeiro da lista:")
l.ver_primeiro()
print("")

print("Vendo o ultimo da lista:")
l.ver_ultimo()
print("")

print("Vendo a quantidade de elementos da lista:")
l.ver_quantidade()
print("")

print("Mostrando se a lista está vazia:")
l.esta_vazia()

print("Removendo um elemento da lista, espera-se: A B D E")
l.remover("B")
print("")
l.show()
l.ver_quantidade()
