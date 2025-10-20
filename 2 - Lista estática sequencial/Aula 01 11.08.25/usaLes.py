import Les

# chamando o módulo, e a classe, e logo, determinando o tamanho maximo, assim como no __init__(self, tamanho)
lista= Les.Les(5)

# Inserindo o valor 4 no final 
lista.inserir_fim(1)
lista.inserir_fim(2)
lista.inserir_fim(3)
lista.inserir_fim(4)
lista.inserir_fim(5)

# Usando o metodo show, para mostrar os valores adicionados
# Saida esperada: 1234
lista.show()

# Inserindo um valor a mais na lista:
# É esperado que ocorra um erro, pois o tamanho da lista é fixo.

#  lista.inserir_fim(6)
# Aqui já imprime com o erro

# removendo o ultimo valor da lista.
# saida esperada: 1234
lista.remover_fim()
lista.show()
# deu certo
