import Les

lista = Les.Les(5)

print("INSERINDO VALORES A, B, D, E NA LISTA.")
lista.inserir_fim("A")
lista.inserir_fim("B")
lista.inserir_fim("D")
lista.inserir_fim("E")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

#===================================================================#

print("INSERINDO O VALOR 'C' APOS O VALOR 'B', ESPERA-SE: A B C D E.")
lista.inserir_apos("B", "C")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

#===================================================================#

print("REMOVENDO O VALOR 'E' DA LISTA, ESPERA-SE: A B C D.")
lista.remover("E")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

#===================================================================#

print("INSERINDO O VALOR 'J' ANTES DO VALOR 'C', ESPERA-SE: A B J C D")
lista.inserir_antes("C", "J")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

#===================================================================#

print("REMOVENDO OS ANTERIORES DE 'J', ESPERA-SE: J C D")
lista.remover_anteriores("J")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

#===================================================================#

print("REMOVENDO TODOS OS VALORES DA LISTA")
lista.remover_anteriores("D")
lista.remover("D")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

#===================================================================#

print("INSERINDO VALORES NA LISTA, ESPERA-SE: A B C D E")
lista.inserir_fim("A")
lista.inserir_fim("B")
lista.inserir_fim("C")
lista.inserir_fim("D")
lista.inserir_fim("E")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

#===================================================================#

print("REMOVENTO TODOS OS VALORES POSTERIORES AO 'C', ESPERA-SE: A B C")
lista.remover_posteriores("C")
lista.get_all_index()
print(f"Capacidade da lista: {lista.get_capacidade()} elementos.")
print(f"Quantidade de elementos na lista: {lista.get_quant()}")
print()

"""print("PEGANDO O INDICE DO VALOR 'A':")
print(lista.get_index("A"))"""

#===================================================================#

print(lista.get_valor(2))
print()
lista.show_reverso()
print()
print(lista.existe("A"))
print(lista.existe("C"))
print(lista.existe("B"))
print(lista.existe("E"))