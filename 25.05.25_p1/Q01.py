# Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

import sys

# Solicitar o número ao usuário:
try:
    numero = int(input('Digite um número de até 4 digitos inteiros e positivos: '))
    if numero < 0 or numero > 9999:
        sys.exit('Digite um número de até 4 digitos inteiro e positivo!')

# Atribuindo as casas numericas:
    mil = numero // 1000
    numero %= 1000

    cem = numero // 100
    numero %= 100

    dez = numero // 10
    numero %= 10

    soma = ( mil + cem + dez + numero )

except ValueError:
    print('ERRO: Informe um valor que possa ser convertido em inteiro')
except Exception as excecao:
    print(f'ERRO: {excecao}')

# Solicitando a soma:
else:
    print(f'A Soma dos digitos de {mil} + {cem} + {dez} + {numero} é: {soma}')