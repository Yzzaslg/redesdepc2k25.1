'''Desenvolva um programa que solicite ao usuário dois valores inteiros: o primeiro representando a quantidade de sub-listas da lista principal e o segundo indicando 
a quantidade de elementos em cada sub-lista. Com base nesses valores, o programa deverá gerar aleatoriamente os elementos de cada sub-lista da lista principal (utilizar 
LIST COMPREHENSIONS), exibir a lista gerada e, em seguida, calcular e apresentar a lista transposta.'''

import sys, random

# Solicitar dados
try:
    n_sublistas = int(input('Informe um valor inteiro ( maior que 0 ) para a quantidade de sub-listas ( linhas ) da lista principal: '))
    n_elementos = int(input('Informe um valor inteiro ( maior que 0 ) para a quantidade de elementos em cada sub-lista: '))
    if n_sublistas <= 0 or n_elementos <= 0:
        sys.exit('Informe um valor inteiro válido.')

except ValueError:
    sys.exit('ERR0: Informe apenas valores inteiros.')
except Exception as e:
    sys.exit(f'ERR0: {e}')

# Criar a lista principal
list_origem = [[random.randint(0, 19) for _ in range(n_elementos)] for _ in range(n_sublistas)] # random.randint vai gerar os elementos dado em () de forma aleatória, primero for in range() vai gerar uma sublista que a quantidade de elementos e o segundo for in range() repete essa sublista várias vezes.


# Criar a lista transposta
list_inversa = [list(verticais) for verticais in zip(*list_origem)] # zip agrupa os elementos de mesma posição, formando novas colunas e o * abre uma lista e retornar cada elemento seu de forma separada.

# Exibir as listas
print('lista origem: ')
for horizontal in list_origem:
    print(horizontal)

print('\nlista inversa: ')
for horizontal in list_inversa:
    print(horizontal)

print('\n--- Fim do programa, obrigado pelo teste!"-" ---')