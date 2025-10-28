import pilhaD

pilha = pilhaD.PilhaD()

pilha.push(10)
pilha.push(20)
pilha.push(30)
print("Pilha após inserções:")
pilha.show()
print("Topo da pilha:", pilha.verTopo())
pilha.pop()
print("Pilha após remoção do topo:")
pilha.show()