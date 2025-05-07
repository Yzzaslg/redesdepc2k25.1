# PROGRAMA PARA CALCULAR TEMPO DO ESPAÇO PERCORRIDO
# DADOS: distancia_ini ( c ) em km, veloc_inicial ( b ) em 'km/h', aceleração ( a ) em 'm/s ** 2', tempo = T em 's'

import sys

distancia_inicial = int(input('Digite o valor da distancia_inicial em km: '))
if distancia_inicial <= 0
    sys.exit('Informe distância positiva')

Veloc_inicial = int(input('Digite o valor da Velocidade_inicial em km/h: '))
if Veloc_inicial <= 0
    sys.exit('Informe velocidade_inicial positiva')

acele_inicial = int(input('Digite o valor da aceleração_inicial em m/s**2: '))
if acele_inicial <= 0
    sys.exit('Informe aceleração_inicial positiva')

distancia_inicial *= 1000
Veloc_inicial /= 3.6

delta = Veloc_inicial ** 2 - 4 * acele_inicial * distancia_inicial
if delta < 0
    sys.exit('Não é possível calcular o tempo')


1h = 60min = 3600s

T = ( a * t ** 2 ) / 2 + v0 * t - d

D = b ** 2 - 4 * a * c