import Lee

lista = Lee.Lee(5)

print('Lista:')
lista.show()
print()
lista.show_vetor()
print()

lista.inserir_inicio('C')
print('Lista após inserir inicio C: (esperado - C)')
lista.show()
lista.show_vetor()

lista.inserir_inicio('D')
print('Lista após inserir inicio D: (esperado - DC)')
lista.show()
print()
lista.show_vetor()

lista.inserir_fim('B')
print('Lista após inserir fim B: (esperado => DCB)')
lista.show()
print()
lista.show_vetor()


lista.remover_inicio()
print('Lista após remover início: (esperado - CB)')
print('Show:')
lista.show()
print('Show vetor:')
lista.show_vetor()


lista.inserir_fim('F') 
print('Lista após inserir fim F: (esperado - CBF)') 
print('Show:') 
lista.show() 
print('Show vetor:') 
lista.show_vetor()
lista.inserir_inicio('E') 
print('Lista após inserir início E: (esperado - ECBF)')
print('Show:') 
lista.show() 
print('Show vetor:') 
lista.show_vetor()
lista.remover_fim() 
print('Lista após remover fim: (esperado - ECB)') 
print('Show:') 
lista.show() 
print('Show vetor:') 
lista.show_vetor()

