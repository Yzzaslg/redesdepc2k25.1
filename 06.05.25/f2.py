# PROGRAMA PARA CALCULAR TEMPO DO ESPAÇO PERCORRIDO
# DADOS: distancia_ini ( c ) em km, veloc_inicial ( b ) em 'km/h', aceleração ( a ) em 'm/s ** 2', tempo = t em 's'

import sys

distancia_inicial = int(input('Digite o valor da distancia_inicial em km: '))
if distancia_inicial <= 0
    sys.exit('Informe distancia positiva')

Veloc_inicial = int(input('Digite o valor da Velocidade_inicial em km/h: '))
if Veloc_inicial <= 0
    sys.exit('Informe velocidade_inicial positiva')

acele_inicial = int(input('Digite o valor da aceleracao_inicial em m/s**2: '))
if acele_inicial <= 0
    sys.exit('Informe aceleracao_inicial positiva')

distancia_inicial *= 1000
Veloc_inicial /= 3.6

delta = Veloc_inicial ** 2 - 4 * acele_inicial * distancia_inicial
if delta < 0
    sys.exit('Não é possível calcular o tempo')

t = ( - Veloc_inicial + delta ** 0.5) / (2 * acele_inicial )

hora = t // 3600

t = t % 3600

minuto = t//60

segundo = t % 60

print(f'tempo = {hora} : {minuto} : {segundo}')