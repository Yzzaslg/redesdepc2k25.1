'''Faça um programa que receba duas strings compostas por 0 e 1 apenas. 
essas strings correspondem a uma sequência binária e devem ter o mesmo comprimento.

Pede-se que após a leitura e a validação das duas strings, o programa apresente o 
resultado das operações lógicas AND, OR e XOR entre essas duas variáveis.'''
 
import sys

# Solictitar as strings.
try:
    string1 = input('Digite uma 1ª sequência binária de 4 digitos: ')
    string2 = input('Digite uma 2ª sequência binária de 4 digitos: ')
    if len(string1) != len(string2): # len() vai verificar o tamanho das strings.
        sys.exit('As strings estão com tamanho diferentes...:/')
except Exception as e:
    sys.exit(f'ERRO: {e}')

# Verificação para as strings conter apenas 0's e 1's, usei for caractere pois verifica cada caractere da string.
else:
    for caractere in string1:
        if caractere not in ('0', '1'):
            sys.exit('Na 1ª string há um caractere inválido...:/')
        
    for caractere in string2:
        if caractere not in ('0', '1'):
            sys.exit('Na 2ª string há um caractere inválido...:/')

# Criar variáveis para os resultados.
operação_AND = ''
operação_OR = ''
operação_XOR = ''

# Percorrer as strings em conjunto.
for posicao in range(len(string1)):
    bit1 = string1[posicao] # Deve usar [] - colchetes, pois servem para acessar elementos em um indice ( posicao ) em strings.
    bit2 = string2[posicao]

# Converter cada caractere bit em inteiro para realizar cálculos com 0 e 1.
    bit1 = int(string1[posicao])
    bit2 = int(string2[posicao])

# Criar as operações lógicas AND [( bit1 & bit2 == 1) = 1, se não é 0], OR [( bit1 == 1 ou bit2 == 1 ) = 1, se não é 0] e 
# XOR [( bit1 != bit2) = 1, se não é 0].
    operação_AND = operação_AND + str(bit1 & bit2) # & - verifica se os dois bits são 1 e retorna 1.
    operação_OR = operação_OR + str(bit1 | bit2) # | - verifica se pelo menos um dos bits é 1 e retorna 1.
    operação_XOR = operação_XOR + str(bit1 ^ bit2) # ^ - compara os dois bits se são diferentes ou iguais, se forem diferentes ele retorna 1.

# Resultados.
print('--- Resultados: ---')
print(f'\nOperação lógica binária AND: {operação_AND}')
print(f'Operação lógica binária OR: {operação_OR}')
print(f'Operação lógica binária XOR: {operação_XOR}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')