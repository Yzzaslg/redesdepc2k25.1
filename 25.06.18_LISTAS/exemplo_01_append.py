'''
   Fazer um programa que solicite ao usuário nomes de pessoas.

   O programa deverá parar de solicitar nomes quando o usuário digitar 'FIM'.

   No final o programa deverá listar os nomes informados.
'''

# Cria a variável do tipo lista
lstNomes = list()

while True:
    # Solicita o nome, removendo espaços em branco a esquerda e a direita.
    strNome = input('Digite um nome: ').strip() # strip retira os espaços direita e esquerda.

    # Verifica se foi digitado 'fim' ( compara em minúscula ) para interromper o laço.
    if strNome.lower() == 'fim':
        break # break vai parar o programa.

    # Se houver caracteres na variável o seu conteúdo será adicionado na lista.
    if len(strNome) > 0: # len é a contagem do tamanho da string.
        lstNomes.append(strNome) # .append adiciona um elemento ao final de uma lista.

# Imprime a lista.
print(lstNomes)