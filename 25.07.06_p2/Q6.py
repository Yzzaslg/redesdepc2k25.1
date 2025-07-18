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
string_numero = string_numero.zfill(4)

# Verificar se todos os digítos são repetidos.
primeiro_digito = string_numero[0]
repetição  = 0

for caractere in string_numero:
    if caractere == primeiro_digito:
        repetição = repetição + 1

if repetição == len(string_numero): # A contagem da repetição de digitos for igual ao tamanho total, todos são iguais.
    sys.exit('A Constante de Kaprekar não é bem sucedida com todos os digitos iguais. ')

iteracoes = 0 # Contador das interacoes
Kaprekar = 0 # Inicialização diferente de 6174 para o loop funcionar.

print('Iterações:')

# Criar o loop que enquanto 'kaprekar' não for igual a 6174 irá continuar rodando.
while Kaprekar != 6174:
    str_num = string_numero

# Criar a ordenação crescente e decrescente.   
# Ordem crescente:
    strcrescente = ''.join(sorted(str_num)) # Sorted = ordena a string em ordem númerica e a transforma em uma lista temp, e .join irá converter essa lista temp em string novamente.

# Ordem decrescente ( inverter a string 'decrescente' ).
    strdecrescente = ''.join(sorted(str_num, reverse=True))

# Convertendo as strings em inteiros.
    num_decrescente = int(strdecrescente)
    num_crescente = int (strcrescente)

# Operação de subtração decresc - cresc = kaprekar.
    Kaprekar = num_decrescente - num_crescente

# Transformar a operação em string e completar com 0's a esquerda.
    resultado_operação = str(Kaprekar).zfill(4)

# Atualização para próxima interação.
    string_numero = resultado_operação
    iteracoes = iteracoes + 1

# Resultado das iterações.
    print(f'Iteração {iteracoes}: {strdecrescente} - {strcrescente} = {resultado_operação}')

# Condição do loop impossível: kaprekar = 0000.
    if Kaprekar == 0:
        sys.exit('O loop se tornou impossível, retornou 0000.')

if Kaprekar == 6174:
    print(f"\nConvergiu para 6174, número de {iteracoes} iterações.")
else:
    print("\nO processo terminou sem convergir para 6174.")

print('\n--- Fim do programa, obrigado pelo teste!"-" ---')