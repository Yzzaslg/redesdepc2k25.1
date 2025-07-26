'''Fazer um programa para gerar automaticamente uma lista (utilizar LIST COMPREHENSIONS) de dimensão de n elementos (n deverá ser solicitado ao usuário e ser positivo), 
com os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente.

Uma vez a lista gerada, implementar as seguintes operações:

i. A média dos valores dos elementos da lista;
ii. A mediana dos valores dos elementos da lista;
iii. A variância populacional dos valores dos elementos da lista;
iv. O desvio-padrão populacional dos valores dos elementos da lista.'''

import sys, random

# Solicitar n ao usuário.
try:
    n = int(input('Informe um número positivo entre 0 e 99: '))
    if n <= 0:
        sys.exit('ERR0: Informe um número positivo válido.')
except ValueError:
    sys.exit('ERR0: Informe apenas valores inteiros.')
except Exception as e:
    sys.exit(f'ERR0: {e}')

# Lista com elementeos entre 0 e 99.
lista = [random.randint(0, 99) for _ in range(n)]

# Cálculo média.
me = 0
for num in lista:
    me += num
media = me / n

# Cálculo mediana.
lista_ordem = sorted(lista)
meio_lista = n // 2 # posição no meio da lista.
if n % 2 == 1: # se retornar 1 ( n impar ): a lista possui uma mediana exata e caso retornar 0 ( n par ): a mediana é dada pela média entre os 2 números do meio.
    mediana = lista_ordem[meio_lista] # acessar a posição da mediana exata.
else:
    mediana = (lista_ordem[meio_lista - 1] + lista_ordem[meio_lista]) / 2 # média das duas posições do meio = mediana.

# Cálculo variância populacional ( mede o quanto os valores de uma lista se espalham em relação à média ).
soma_dife_quad = 0
for num in lista:
    dif = num - media # diferença entre o número da lista e a média.
    soma_dife_quad += dif ** 2
variacao = soma_dife_quad / n # dividir a soma dos quadrados das diferenças pela quantidade total de elementos.

# Cálculo desvio-padrão populacional ( dado por √variância populacional ).
desvio_padrao = variacao ** 0.5

print(f'Desvio-padrão populacional: {desvio_padrao:.1f}')

print(f'\nLista: {lista}')
print(f'Lista ordenada: {lista_ordem}')
print('\nResultados das operarações: ')
print(f'Média: {media:.1f}')
print(f'Mediana: {mediana:.1f}')
print(f'Variância populacional: {variacao:.1f}')
print(f'Desvio-padrão populacional: {desvio_padrao:.1f}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')