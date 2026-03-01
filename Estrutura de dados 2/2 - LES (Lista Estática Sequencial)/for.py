lista = [1, 2, 3, 4, 5]
for i in range(len(lista)):
    if lista[i] == 3:
        cont = 0
        print(i)
        for j in range(i, len(lista) - 1):
            cont += 1
        print(cont)