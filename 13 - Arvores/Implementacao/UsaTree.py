import Tree

t1 = Tree.Tree()

t1.inserir(4)
t1.inserir(2)
t1.inserir(6)
t1.inserir(7)
t1.inserir(1)
t1.inserir(5)
t1.inserir(3)

print("Buscando um valor na árvore.")

t1.busca(7)

print("In ordem:")
print(t1.inOrdem())