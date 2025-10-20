import Ldde

l = Ldde.Ldde()

l.inserir_fim('A')
l.inserir_fim('B')
l.inserir_fim('C')
l.inserir_fim('D')
l.inserir_fim('E')
l.inserir_fim('F')
l.inserir_fim('G')
l.inserir_fim('H')
l.inserir_fim('I')
l.inserir_fim('J')
l.inserir_fim('K')
l.inserir_fim('L')
l.show() # ABCDEFGHIJKL
# l.show_reverso() # LKJIHGFEDCBA
print("")





print("Vizinhos de 'F' (meio): remove 'E' e 'G'")
l.remover_vizinhos('F')
l.show() # ABCDFHIJKL
l.show_reverso() # LKJIHFDCBA
print("")



print("Vizinhos de 'A' : remove apenas 'B'")
l.remover_vizinhos('A')
l.show() # ACDFHIJKL
l.show_reverso() # LKJIHFDCA
print("")



print("Vizinhos de 'L' : remove apenas 'K'")
l.remover_vizinhos('L')
l.show() # ACDFHIJL
l.show_reverso() # LJIHFDCA
print("")


print("Vizinhos de 'C' : remove 'A' e 'D'")
l.remover_vizinhos('C')
l.show() # CFHIJL
l.show_reverso() # LJIHFC
print("")


print("Insrindo 'A' no início")
l.inserir_inicio('A')
l.show() # ACFHIJL
l.show_reverso() # LJIHFCA
print("")


print("Vizinhos de 'J' : remove 'I' e 'L'")
l.remover_vizinhos('J')
l.show() # ACFHJ
l.show_reverso() # JHFCA
print("")


print("Insrindo 'L' no fim")
l.inserir_fim('L')
l.show() # ACFHJL
l.show_reverso() # LJHFCA
print("")


print("Valor inexistente 'X' (não altera)")
l.remover_vizinhos('X')
l.show() # ACFHJL
l.show_reverso() # LJHFCA
