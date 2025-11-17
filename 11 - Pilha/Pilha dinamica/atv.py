import pilhaD

def inverter_palavra(palavra):
    pilha = pilhaD.PilhaD()

    # empilha letra por letra
    for letra in palavra:
        pilha.push(letra)

    invertida = ""

    # desempilha reconstruindo
    while not pilha.vazia():
        invertida += pilha.pop()

    return invertida


def main():
    frase = input("Digite uma frase: ")

    palavras = frase.split()  # permitido

    resultado = ""  # frase final

    for i in range(len(palavras)):
        palavra_invertida = inverter_palavra(palavras[i])

        # adiciona um espaço **somente depois das palavras, menos a última**
        if i == 0:
            resultado += palavra_invertida
        else:
            resultado += " " + palavra_invertida

    print("Saída:", resultado)


main()
