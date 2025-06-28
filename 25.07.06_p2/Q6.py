'''Tomando por base a definição de Constante de Kaprekar (https://pt.wikipedia.org/wiki/Constante_de_Kaprekar) faça um programa que receba um inteiro positivo de no máximo 
4 dígitos e exiba em quantas iterações esse número converge para a Constante de Kaprekar. Exiba as iterações também.

Para que um número de 4 dígitos não convirja para 6174, a restrição a ser considerada é a seguinte: número tiver todos os seus dígitos iguais, como 1111, 2222, 3333, etc., 
o processo de Kaprekar não funcionará, porque a diferença entre o número maior (formado pelos dígitos em ordem decrescente) e o menor (formado pelos dígitos em ordem crescente)
será sempre zero.

Por exemplo:

para n = 3524, o programa deverá exibir a seguinte saída:

Iterações:
5432 – 2345 = 3087
8730 – 0378 = 8352
8532 – 2358 = 6174

Nº de Iterações: 3'''

import sys

# Solicitar um número inteiro positivo
try:
    numero = int(input('Digite um número inteiro ( no máximo 4 dígitos ): '))
    if numero <= 0 or numero > 9999:
        sys.exit('Digite um número positivo e ter no máximo 4 digitos...')
except ValueError:
    sys.exit('Informe apenas valores reais...')
except Exception as e:
    sys.exit(f'ERRO: {e}')

# Transformar o número em string para verificação de número com apenas digitos repetidos.
else:
    string_numero = str(numero)

# Completar o número com 0's a esquerda.
    tamanho  = len(string_numero)
    Q_zeros = 4 - tamanho

# Criar a string para completar os zeros.
    zero = ''
    for posicao in range(Q_zeros):
        zeros = zeros + '0'

# Adicionar os 0's a string_numero agora.
string_numero = zeros + string_numero

# Verificar se todos os digítos são repetidos.
primeiro_digito = string_numero[0]
repetição  = 0

for caractere in string_numero:
    if caractere == primeiro_digito:
        repetição = repetição + 1

if repetição == len(string_numero): # A contagem da repetição de digitos for igual ao tamanho total, todos são iguais.
    sys.exit('A Constante de Kaprekar não é bem sucedida com todos os digitos iguais. ')






