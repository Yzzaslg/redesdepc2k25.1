# PROGRAMA PARA CALCULAR MOVIMENTO RETÍLIO E SOLICITAR OS VALORES AO USUÁRIO
# DADOS: veloc_inicial em 'm/s', aceleração em 'm/s ** 2', tempo em 's'

from os import system
import sys

veloc_inicial = int(input('Digite o valor de veloc_inicial em m/s: '))
if veloc_inicial <=0:
    sys.exit('Informe velocidade positiva')

aceleração = int(input('Digite o valor da aceleração em m/s ** 2: '))
if aceleração <=0:
    sys.exit('Informe aceleração positiva')

tempo = int(input('Digite o valor do tempo em s: '))
if tempo <=0:
    sys.exit('Informe tempo positivo')

DS = veloc_inicial * tempo + ( ( aceleração * tempo ** 2) / 2 )

print(f'O Valor de ΔS é {DS} em m/s')