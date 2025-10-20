from Lee import Lee

lista = Lee(6)

print('Lista inicial (esperado: vazia)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Inserir no início
lista.inserir_inicio('A')
print('Após inserir início A (esperado: A)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

lista.inserir_inicio('B')
print('Após inserir início B (esperado: B A)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Inserir no fim
lista.inserir_fim('C')
print('Após inserir fim C (esperado: B A C)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Remover elemento específico
lista.remover_elemento('A')
print('Após remover A (esperado: B C)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Buscar elementos
print('Buscar B (esperado: posição 0) ->', lista.buscar('B'))
print('Buscar C (esperado: posição 1) ->', lista.buscar('C'))
print('Buscar X (esperado: None) ->', lista.buscar('X'))
print('-' * 40)

# Inserir após
lista.inserir_apos('D', 'B')
print('Após inserir D depois de B (esperado: B D C)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Inserir antes
lista.inserir_antes('E', 'C')
print('Após inserir E antes de C (esperado: B D E C)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Inserir antes do primeiro
lista.inserir_antes('F', 'B')
print('Após inserir F antes de B (esperado: F B D E C)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Remover fim
lista.remover_fim()
print('Após remover fim (esperado: F B D E)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)

# Remover início
lista.remover_inicio()
print('Após remover início (esperado: B D E)')
lista.show()
print()
lista.show_vetor()
print('-' * 40)
