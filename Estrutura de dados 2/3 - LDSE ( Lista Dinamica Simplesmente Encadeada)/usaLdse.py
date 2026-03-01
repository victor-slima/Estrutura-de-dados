import Ldse

lista = Ldse.Ldse()

#===========================================================================#

print("ADICIONANDO NO INICIO OS VALORES E D C B A, ESPERA-SE: A B C D E.")
lista.inserir_inicio("E")
lista.inserir_inicio("D")
lista.inserir_inicio("C")
lista.inserir_inicio("B")
lista.inserir_inicio("A")
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("REMOVENDO NO INICIO OS VALORES A B C, ESPERA-SE: D E.")
lista.remover_inicio()
lista.remover_inicio()
lista.remover_inicio()
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("INSERINDO O VALOR E, F, G NO FINAL DA LISTA, ESPERA-SE: A B C D E F G H.")
print()
lista.inserir_fim("F")
lista.inserir_fim("G")
lista.inserir_fim("H")
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("INSERINDO NOVAMENTE A B C NO INICIO DA LISTA, ESPERA-SE: A B C D E F G H.")
lista.inserir_inicio("C")
lista.inserir_inicio("B")
lista.inserir_inicio("A")
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("REMOVENDO O VALOR FINAL DA LISTA, ESPERA-SE: A B C D E F G.")
lista.remover_fim()
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("REMOVENDO OS IRMAOS DE A, ESPERA-SE A C D E F G.")
lista.remover_irmaos("A")
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("REMOVENDO O VALOR D DA LISTA, ESPERA-SE: A C E F G.")
lista.remover("D")
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("INSERINDO 'K' APOS O 'A', E 'U' APOS O 'C', ESPERA-SE: A K C U E F G.")
lista.inserir_apos("K", "A")
lista.inserir_apos("U", "C")
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()

#===========================================================================#

print("INSERINDO O VALOR 'H' ANTES DO 'G', E 'R' ANTES DO 'A', ESPERA-SE: R A K C U E F H G")
lista.inserir_antes("H", "G")
lista.inserir_antes("R", "A")
lista.show()
print(f"Primeiro nó da lista: {lista.ver_primeiro()}")
print(f"Ultimo nó da lista: {lista.ver_ultimo()}")
print(f"{lista.get_quant()}")
print()