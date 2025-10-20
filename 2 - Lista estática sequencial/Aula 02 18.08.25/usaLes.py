import Les

# Criando uma variavel, e inserindo nela o nome do arquivo fonte, e no nome da classe, e ja definindo
# o tamanho do vetor, que está em self.
array = Les.Les(5)

# Chamando o método show(), saída esperada: None None None None None
print("Chamando o método show(), saída esperada: None None None None None")
array.show()
print()

# Utilizando agora o método de inserir_fim, saida esperada: A B C D E
print("Utilizando agora o método de inserir_fim, saida esperada: A B C D E")
array.inserir_fim("A")
array.inserir_fim("B")
array.inserir_fim("C")
array.inserir_fim("D")
array.inserir_fim("E")
array.show()
print()


# Utilizando agora o método de inserir_inicio, saída esperada: A B C
print("Utilizando agora o método de inserir_inicio, saída esperada: A B C")
array.remover_fim()
array.remover_fim()
array.show()
print()

# Utilizando agora o método de inserir_inicio, saída esperada: E D A B C
print("Utilizando agora o método de inserir_inicio, saída esperada: E D A B C")
array.inserir_inicio("D")
array.inserir_inicio("E")
array.show()
print()

# Utilizando agora o método de remover_inicio, saída esperada: A B C
print("Utilizando agora o método de remover_inicio, saída esperada: A B C")
array.remover_inicio()
array.remover_inicio()
array.show() 
print()

# Inserindo novamente,no final do vetor, os valores "D" e "E".
# Saída esperada: A B C D E
print("Inserindo novamente,no final do vetor, os valores 'D' e 'E' \n"
"Saída esperada: A B C D E:")
array.inserir_fim("D")
array.inserir_fim("E")
array.show()
print()

# Utilizando agora o método que remove um valor que o usuario inserir:
# Saída esperada: A B D E
print("Utilizando agora o método que remove um valor que o usuario inserir:\n" \
"Saída esperada A B D E:\n")
array.remover("C")
array.show()
print()

# Utilizando agora o método que removerTF:
print("Utilizando agora o método que removerTF.\n" \
"Saída esperada: True\n")

array.removerTF("A")
array.show()
print()

# Removendo todos os valores:
array.remover("B")
array.remover("D")
array.remover("E")
array.show()
print()

# COLOCANDO AS INSTRUCOES ACIMA DENTRO DE COMENTARIO
# Inserindo valores dentro do vetor, para teste do método remover_contar.
array.inserir_inicio("E")
array.inserir_inicio("E")
array.inserir_inicio("B")
array.inserir_inicio("B")
array.inserir_inicio("A")
print("Inserindo valores dentro do vetor, para teste do método remover_contar.")
print("Saída esperada: A B B E E")
array.show()
print()

# Tentando usar o método remover_contar:
array.remover_contar("E")
print("Saida esperada: A B B.")
array.show()
print()

array.remover_contar("E")
print("Saída esperada: NADA.")
array.show()
print()

array.remover_contar("B")
print("Saida esperada: A.")
array.show()
print()