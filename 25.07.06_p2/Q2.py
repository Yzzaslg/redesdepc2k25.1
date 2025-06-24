"""Existem somente quatro números, maiores do que um, que podem ser obtidos
pela soma de potências de 4 dos seus digitos:

1643 = 1^4 + 6^4 + 4^4 + 3^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

Faça um programa que encontra e exibe os números menores de 1000000, que são 
múltiplos de 2 ou 5 e que podem ser escritos pela soma das potências de 5 de
seus dígitos."""

import sys

numBase = int(input('Digite um número inteiro como base: '))
numPotencia = 5
