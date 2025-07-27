'''Implemente o algoritmo do Crivo de Eratóstenes em Python para encontrar todos os números primos 
menores ou iguais a um número n. O número n será fornecido como entrada.

INSTRUÇÕES:

i. Utilize uma lista para marcar os números como primos ou não primos;
ii. Implemente a marcação dos múltiplos como não primos de acordo com o Crivo de Eratóstenes
iii. A entrada será um número inteiro n (2 ≤ n ≤ 10**6);
iv. Ao final, imprima a lista com todos os números primos encontrados.'''

import sys

# Solicitar n.
try:
    n = int(input('Informe um número positivo e entre 2 e 10**6 ( 1.000.000 ): '))
    if n < 2 or n > 10**6:
        sys.exit('ERR0: Informe um número positivo válido.')
except ValueError:
    sys.exit('ERR0: Informe apenas valores inteiros.')
except Exception as e:
    sys.exit(f'ERR0: {e}')

# Criar lista de 2 até n.
lista_numeros = []
for i in range(n + 1):
    lista_numeros.append(1) # se inicia a lista com todos os elementos em 1 ( primos ).
lista_numeros[0] = 0 # registrar 0 e 1 como não primos.
lista_numeros[1] = 0

# Crivo de Eratóstenes = O(n√n)
i = 2 # começa em 2
for i in range(2, int(n**0.5) + 1): # loop para testar os números como primos.
    if lista_numeros[i] == 1:
        for j in range(i * i, n + 1, i): # loop para testar os múltiplos dos números e marcar como não primos ( = 0 ).
            lista_numeros[j] = 0

# Criar lista de números primos e não primos.
lista_primos = []
lista_nao_primos = []
for i in range(2, n + 1 ):
    if lista_numeros[i] == 1:
        lista_primos.append(i)
    else:
        lista_nao_primos.append(i)

# Resultado da lista
print('Listas: ')
print(f'\nNúmeros primos: {lista_primos}')
print(f'Números não primos: {lista_nao_primos}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')






        



