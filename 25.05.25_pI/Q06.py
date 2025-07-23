'''Desenvolva um um programa que efetue as seguintes especificações:

Solicite ao usuário os comprimentos dos três lados do triângulo;
Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe que não é possível formar um triângulo com esses lados;
Se for possível formar um triângulo, calcule os três ângulos do triângulo;
Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno);
Classifique o triângulo quanto os ângulos (acutângulo, obtusângulo ou retângulo);'''

import sys
import math

try:
    lado_a = int(input('Informe o lado A do triângulo: '))
    lado_b = int(input('Informe o lado B do triângulo: '))
    lado_c = int(input('Informe o lado C do triângulo: '))

# A soma de quaisquer dois lados de um triângulo deve ser sempre maior que o terceiro lado:
    if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
        print('os lados formam um triângulo')
    else:
        sys.exit('os lados não formam um triângulo')

# Cálculo dos ângulos com math.degrees ( converte radianos em graus ) e math.acos ( cálcula o ângulo cujo cosseno é igual ao valor fornecido em radianos ),
# e com o uso da lei dos cossenos ( pois temos os valores dos 3 lados e precisamos cálcular os ângulos ).
    ang_a = int(round(math.degrees(math.acos((lado_b**2 + lado_c**2 - lado_a**2) / (2 * lado_b * lado_c))))) # (b**2 + c**2 - a**2) / (2 * b * c) para a, nos demais é só trocar o ângulo.
    ang_b = int(round(math.degrees(math.acos((lado_a**2 + lado_c**2 - lado_b**2) / (2 * lado_a * lado_c)))))
    ang_c = int(round(180 - ( ang_a + ang_b ))) # soma dos 3 ângulos deve ser igual a 180º, então C será a diferença entre 180 menos a soma dos outros 2 ângulos.
    if (ang_a <= 0) or (ang_b <= 0) or (ang_c <= 0):
        sys.exit('Um ou mais ângulos não são positivos.')
    if ang_a + ang_b + ang_c != 180:
        sys.exit('A soma dos ângulos deve ser 180º.')
    else:
        print(f'Os ângulos cálculos são: {ang_a}º, {ang_b}º e {ang_c}º')

# Classifique o triângulo quanto os ângulos (acutângulo, obtusângulo ou retângulo):
# Acutângulo ( todos os ângulos < 90º ), obtusângulo ( um ângulo > 90º ) e retângulo ( um ângulo = 90º ).
    if ang_a == 90 or ang_b == 90 or ang_c == 90:
        print('O triângulo é Retângulo.')
    elif ang_a > 90 or ang_b > 90 or ang_c > 90:
        print('O triângulo é Obtusângulo.')
    else:
        print('O triângulo é Acutângulo.')

# Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno):
# Equilátero ( todos os lados iguais ), isósceles ( dois lados iguais ) e escaleno ( todos os lados diferentes ).
    if lado_a == lado_b == lado_c:
        print('O Triângulo é Equilátero.')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('O Triângulo é Isósceles.')
    else:
        print('O Triângulo é Escaleno.')

except ValueError:
    sys.exit('Digite apenas valores reais.')
except Exception as excecao:
    print(f'ERRO: {excecao}')