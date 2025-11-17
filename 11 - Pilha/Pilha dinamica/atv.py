import pilhaD

def ver_palindromo(palavra):
    palavra = "".join(palavra.split())
    pilha = pilhaD.PilhaD()

    for char in palavra:
        pilha.push(char)

    for char in palavra:
        if pilha.verTopo() != char:
            return False
        pilha.pop()

    return True

print(ver_palindromo("socorram me subi no onibus em marrocos"))
