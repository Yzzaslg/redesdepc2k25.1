'''Na definição da Wikipédia, número de Armstrong é aquele número cuja soma de cada digito dele elevado a potência n (onde n é a quantidade de dígitos) 
é igual ao número informado (veja a definição detalhada em https://en.wikipedia.org/wiki/Narcissistic_number).

Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) um número de Armstrong, de acordo com a definição. 
NÃO usar a função LEN().'''

import sys

# Solicitar o número ao usuário.
try:
    num = int(input('Informe um número inteiro positivo: '))
    if num <= 0:
        sys.exit('O Número deve ser positivo!')
except ValueError:
    sys.exit('Informe apenas valores reais para o número.')
except Exception as e:
    sys.exit(f'ERRO: {e}')

# Contar quantos dígitos tem o número o dado
else:
    num_temp = num
    pot_qt_digitos = 0
while num_temp > 0:
    num_temp = num_temp // 10
    pot_qt_digitos = pot_qt_digitos + 1
    soma = 0

# Converter para string 'digito'.
for digito in str(num):

# Realizar a soma com a potência "a**n" ( potência quantidade de digitos = pot_qt_digitos ).
    valor = int(digito) ** (pot_qt_digitos) # valor é os digitos convertidos em inteiros e elevados pela quantidade de digitos.
    soma = soma + valor

print(f'Valor da soma é: {soma}') # Deixei esse print só para verificação de valores.

# Verificando se o número é ou não de Armstrong.
if soma == num:
    print(f'{num} é um número de Armstrong!')
else:
    print(f'{num} não é um número de Armstrong!')

print('--- Fim do programa, obrigado pelo teste! =D ---')