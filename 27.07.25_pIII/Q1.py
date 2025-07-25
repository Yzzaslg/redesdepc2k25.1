'''Desenvolva um programa que solicite ao usuário dois valores inteiros: o primeiro representando a quantidade de sub-listas da lista principal e o segundo indicando 
a quantidade de elementos em cada sub-lista. Com base nesses valores, o programa deverá gerar aleatoriamente os elementos de cada sub-lista da lista principal (utilizar 
LIST COMPREHENSIONS), exibir a lista gerada e, em seguida, calcular e apresentar a lista transposta.'''

import sys, random

# Solicitar dados
try:
    n_linhas = int(input('Informe um valor inteiro ( maior que 0 ) para a quantidade de linhas ( sub-listas ) da lista principal: '))
    n_colunas = int(input('Informe um valor inteiro ( maior que 0 ) para a quantidade de colunas em cada sub-lista: '))
    if n_linhas <= 0 or n_colunas <= 0:
        sys.exit('Informe um valor inteiro válido.')

except ValueError:
    sys.exit('ERR0: Informe apenas valores inteiros.')
except Exception as e:
    sys.exit(f'ERR0: {e}')

# Criar a lista principal
list_origem = [[random.randint(0, 19) for _ in range(n_colunas)] for _ in range(n_linhas)] # random.randint vai gerar os elementos dado em () de forma aleatória, primero for in range() vai gerar uma sublista com a quantidade de elementos e o segundo for in range() repete essa sublista várias vezes.


# Criar a lista transposta
list_inversa = [[list_origem[l][c] for l in range(n_linhas)] for c in range(n_colunas)] # loop externo percorre as colunas da lista geral e o interna as linhas, list_origem[l (linha)][c (coluna)] acessa a posição invertida do elemento, criando a transposta.

# Exibir as listas
print('lista origem: ')
for horizontal in list_origem:
    print(horizontal)

print('\nlista transposta: ')
for horizontal in list_inversa:
    print(horizontal)

print('\n--- Fim do programa, obrigado pelo teste!"-" ---')
