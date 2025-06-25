"""Existem somente quatro números, maiores do que um, que podem ser obtidos pela soma de potências de 4 dos seus digitos:

1643 = 1^4 + 6^4 + 4^4 + 3^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

Faça um programa que encontra e exibe os números menores de 1000000, que são múltiplos 
de 2 ou 5 e que podem ser escritos pela soma das potências de 5 de seus dígitos."""

import sys

# Laço para averiguar se o número está entre 2 e 1000000
for num in range(2, 1000000):

# Condição para o número ser múltiplo de 2 ou 5.
    if num % 2 == 0 or num % 5 == 0:
        soma = 0 # A variação soma se inicia em 0, pois irá armazenar a soma dos digitos.

# Convertendo a variável 'num' em string para que se possa utilizar cada digito de forma individual.
        for digito in str(num): 
            valor = int(digito) ** 5  # Cada digito será convertido em inteiro e elevado a potência 5.
            soma =  soma + valor

# Condição para verificar se a soma é igual ao número inicial, se sim, o 'num' será impresso no terminal.
        if soma == num:
            print(num)
