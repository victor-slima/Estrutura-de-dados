import Ldse

l = Ldse.Ldse()

l.inserir_inicio("B")
l.inserir_inicio("A")
l.inserir_inicio("C")

print("INSERINDO INICIO, B A C, SAÍDA ESPERADA: C A B.")
l.show()
print()

l.inserir_fim("I")
l.inserir_fim("D")
l.inserir_fim("E")
print("INSERINDO FIM, I D E, SAÍDA ESPERADA: C A B I D E.")
l.show()
print()

l.remover_inicio()
print("REMOVENDO O PRIMEIRO NÓ DA LISTA")
l.show()
print()

print("VENDO O PRIMEIRO DA LISTA:")
print(l.ver_primeiro())
print()

print("VENDO O ÚLTIMO DA LISTA:")
print(l.ver_ultimo())
print()