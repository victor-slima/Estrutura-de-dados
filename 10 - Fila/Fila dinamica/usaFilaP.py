import FilaP

# Criando a fila de prioridade
fila = FilaP.FilaP()

# Inserir 5 elementos
fila.inserir("Paciente Grávida 1", 2)
fila.inserir("Paciente Idoso 1", 1)
fila.inserir("Paciente Deficiente 1", 3)
fila.inserir("Paciente Idoso 2", 1)
fila.inserir("Paciente Normal 1", 4)

print("Próximo a ser atendido:", fila.ver_primeiro())
fila.show()

# Remover 2 elementos
fila.remover()
fila.remover()
print("Próximo a ser atendido:", fila.ver_primeiro())
fila.show()

# Inserir mais 3 elementos
fila.inserir("Paciente Grávida 2", 2)
fila.inserir("Paciente Idoso 3", 1)
fila.inserir("Paciente Deficiente 2", 3)
print("Próximo a ser atendido:", fila.ver_primeiro())
fila.show()

# Remover 1 elemento
fila.remover()
print("Próximo a ser atendido:", fila.ver_primeiro())
fila.show()

# Inserir mais 4 elementos
fila.inserir("Paciente Normal 2", 4)
fila.inserir("Paciente Grávida 3", 2)
fila.inserir("Paciente Idoso 4", 1)
fila.inserir("Paciente Deficiente 3", 3)
print("Próximo a ser atendido:", fila.ver_primeiro())
fila.show()

# Remover até esvaziar
while not fila.vazia():
    fila.remover()
    print("Próximo a ser atendido:", fila.ver_primeiro())
    fila.show()
