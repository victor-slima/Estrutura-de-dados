# FUNCAO QUE CRIA UMA LISTA COM 11 VALORES FALSE:
def criar():
    lista = [False] * 11
    return lista

# FUNCAO QUE MOSTRA A LISTA:
def show(lista):
    for i in range(11):
        if lista[i]:
            print(i)

# FUNCAO QUE INSERE UM VALOR NA LISTA:
def inserir(num, lista):
    if num >= 0 and num <= 10:
        lista[num] = True
    else:
        print("Valor invalido")

# FUNCAO QUE REMOVE UM VALOR NA LISTA:
def remover(num, lista):
    if num >= 0 and num <= 10:
        lista[num] = False
    else:
        return "Valor inválido"

# FUNCAO QUE REALIZA A UNIAO ENTRE DUAS LISTAS:
def uniao(listaA, listaB):
    listaC = criar()
    for i in range(11):
        listaC[i] = listaA[i] or listaB[i]
    return listaC

# FUNCAO QUE REALIZA A INTERSECÇAO ENTRE DUAS LISTAS:
def inter(listaA, listaB):
    listaC = criar()
    for i in range(11):
        listaC[i] = listaA[i] and listaB[i]
    return listaC
#__________________________________________________
lista = criar()
inserir(2,lista)
print('Apresentando lista após inserir o valor 2:')
show(lista)
inserir(6,lista)
print('Apresentando lista após inserir o valor 6:')
show(lista)
remover(2,lista)
print('Apresentando lista após remover o valor 2:')
show(lista)
#__________________________________________________
lista1 = criar()
lista2 = criar()
inserir(2, lista1)
inserir(4, lista1)
inserir(7, lista1)
inserir(3, lista2)
inserir(5, lista2)
inserir(7, lista2)
lista3 = uniao(lista1, lista2)
print("lista 1: ")
show(lista1)
print("lista 2: ")
show(lista2)
print("Uniao entre as duas listas: ")
show(lista3)

lista4 = inter(lista1, lista2)
print("Lista 4: (intersecao entre as duas listas)")
show(lista4)