# PROGRAMA PARA CLASSIFICAR UM TRIÂNGULO QUANTO AOS ÂNGULOS.

# O PROGRAMA DEVERÁ SOLICITAR 3 ÂNGULOS INTEIROS POSITIVOS;
# PARA SER UM TRIÂNGULO, A SOMA DOS ÂNGULOS DEVE SER IGUAL A 180;

# RETÂNGULO: POSSUI UM ÂNGULO INTERNO RETO (IGUAL A 90).
# OBTUSÂNGULO: POSSUI UM ÂNGULO INTERNO OBTUSO (MAIOR QUE 90).
# ACUTÂNGULO: POSSUI TODOS OS ÂNGULOS INTERNOS AGUDOS(MENORES QUE 90).

import sys

ang1 = int(input('Informe o ângulo 1 do triângulo: '))
ang2 = int(input('Informe o ângulo 2 do triângulo: '))
ang3 = int(input('Informe o ângulo 3 do triângulo: '))

# Verificando se os ângulos são positivos
if (ang1 <= 0) or (ang2 <= 0) or (ang3 <= 0):
    sys.exit('ERRO: Um ou mais ângulos não são positivos.')

#Verificando se a soma dos ângulos é igual a 180
if ang1 + ang2 + ang3 != 180:
    sys.exit('ERRO: A soma dos ângulos deve ser 180.')

#Classificar o triângulo com base nos ângulos
if ang1 == 90 or ang2 == 90 or ang3 == 90:
    print('O triângulo é Retângulo.')
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print('O triângulo é Obtusângulo.')
else:
    print('O triângulo é Acutângulo.')




