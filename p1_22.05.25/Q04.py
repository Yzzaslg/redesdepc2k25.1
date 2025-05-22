'''Considerando uma equação do 2º grau na forma:

a*(x**2) + b*x + c = 0


Onde a, b e c são coeficientes reais, e x representa a variável que queremos encontrar.



Considerando que as raízes dessa equação são encontradas através da fórmula de Bhaskara.


x = b**2 +- ( delta ** 0.5 ) / 2*a


E que o valor de delta é dado por:


delta = b*2 - 4*a*c

Com base no valor de delta temos as seguintes condições:

delta maior que zero, a equação tem duas raízes reais distintas;
delta igual a zero, a equação tem uma raiz real (ou duas iguais);
delta menor que zero, a equação não tem raízes reais.

Elabore um programa que solicite ao usuário os coeficientes da equação (a, b e c) e exiba as raízes reais da equação (quando houver).'''

import sys

# Solicitar os coeficientes para o usuário:
try:    
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    if a == 0:
        sys.exit('Não é uma equação de 2º grau ( "a" não pode ser == 0).')

# Descobrir o valor de delta
    else:
        delta = b**2  - 4*a*c
        print(f'Delta = {delta:.2f}')

# Descobrir a quantidade de raizes reais:
    if delta < 0:
        print('Na equação não se encontra nenhuma real.')
    elif delta == 0:
        x = -b / ( 2 * a )
        print(f'Na equação se encontra uma raiz real: x = {x:.2f}')
    else:
        raiz_delta = delta ** 0.5
        x1 = ( -b + raiz_delta ) / ( 2*a )
        x2 = ( -b - raiz_delta ) / ( 2*a )
        print('Na equação se encontra duas raizes reais:')
        print(f'x1 = {x1:.2f} e x2 = {x2:.2f}')

except ValueError:
    print('Informe um valor válido')