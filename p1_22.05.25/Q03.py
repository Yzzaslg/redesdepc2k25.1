'''Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo.


Faça um programa que solicite ao usuário:

O momento inicial da partida (no formato HH:MM);
O momento de chegada (no formato HH:MM);
O tempo parado para descanso (no formato HH:MM);
A quantidade de litros de combustível gasto;
O preço do litro de combustível (em R$) e;
A distância percorrida (em Km);

Após receber os dados, o programa informa dados típicos de um computador de bordo:

O tempo de viagem (no formato HH:MM:SS);
A velocidade média (Km/h) global e a velocidade média em movimento (Km/h);
O custo da viagem com combustível (em R$);
O desempenho do carro (em Km/l, l/h e R$/Km).'''

import sys

# Solicitando dados
# Horário momento inicial:
print('Informe o tempo do momento inicial em HH:MM:')
try:
    partida_h = int(input('Digite as horas ( de 0h a 23h): '))
    if partida_h < 0 or partida_h > 23:
        sys.exit('Digite um valor entre 0 e 23 para as horas!')
    partida_min = int(input('Digite os minutos ( de 0min a 59min ): '))
    if partida_min < 0 or partida_min > 59:
        sys.exit('Digite um valor entre 0 e 59 para os minutos!')
    print(f'Horário de partida: {partida_h:02d}:{partida_min:02d}')

# Horário momento final:
    print('Informe tempo do momento final em HH:MM:')
    chegada_h = int(input('Digite as horas ( de 0h a 23h): '))
    if chegada_h < 0 or chegada_h > 23:
        sys.exit('Digite um valor entre 0 e 23 para as horas!')
    chegada_min = int(input('Digite os minutos ( de 0min a 59min ): '))
    if chegada_min < 0 or chegada_min > 59:
        sys.exit('Digite um valor entre 0 e 59 para os minutos!')
    print(f'Horário de chegada: {chegada_h:02d}:{chegada_min:02d}')

# Horário de descanso:
    print('Informe tempo parado para descanso em HH:MM:')
    descanso_h = int(input('Digite as horas ( de 0h a 23h): '))
    if descanso_h < 0 or descanso_h > 23:
        sys.exit('Digite um valor entre 0 e 23 para as horas!')
    descanso_min = int(input('Digite os minutos ( de 0min a 59min ): '))
    if descanso_min < 0 or descanso_min > 59:
        sys.exit('Digite um valor entre 0 e 59 para os minutos!')
    print(f'Horário de descanso: {descanso_h:02d}:{descanso_min:02d}')

except ValueError:
    sys.exit('Digite apenas valores inteiros para horas e minutos.')

# Converter os valores para minutos 
movi_ini_min = partida_h * 60 + partida_min
movi_fin_min = chegada_h * 60 + chegada_min
tempo_descanso_min = descanso_h * 60 + descanso_min

# Condição da chegada ser no outro dia
if movi_fin_min < movi_ini_min:
    movi_fin_min = movi_fin_min + 24*60 # 24*60 = dia total em minutos :)

# Calculando o tempo da viagem total e em movimento
tempo_viagem_total_min = movi_fin_min - movi_ini_min
tempo_movi_total_min = tempo_viagem_total_min - tempo_descanso_min

# Mais dados da viagem
try:
    comb_litros = float(input('Digite a quantidade de combustível gasto ( em litros ): '))
    comb_valor = float(input('Digite o valor do litro do combustível:R$ '))
    distancia = float(input('Digite o valor da distância ( em km ): '))
    if comb_litros < 0 or comb_valor < 0 or distancia < 0:
        sys.exit('Digite apenas valores positivos!')

except ValueError:
    sys.exit('Digite apenas valores reais para combustivel em litros, valor do combustível e distância.')

# Converter o tempo em horas
tempo_viagem_total_h = tempo_viagem_total_min / 60
tempo_movi_total_h = tempo_movi_total_min / 60

# Velocidade média da viagem
if tempo_viagem_total_h > 0:
    vel_media_viagem = distancia / tempo_movi_total_h
else:
    vel_media_viagem = 0

# Tempo em movimento e combustivel gasto em litros
if tempo_movi_total_h > 0:
    vel_media_movi = distancia / tempo_movi_total_h
    comb_litros_por_h = comb_litros / tempo_movi_total_h
else:
    vel_media_movi = 0
    comb_litros_por_h = 0

# Calculo do desempenho durante a viagem
if comb_litros > 0:
    desempenho_em_km_l = distancia / comb_litros
else: 
    desempenho_em_km_l = 0

# Calculo dos custos do combustivel
if distancia > 0:
    custo_por_km = ( comb_litros * comb_valor ) / distancia
else:
    custo_por_km = 0

custo_total_viagem = comb_litros * comb_valor

# Finalizando o código, formatando os tempos em HH:MM:SS
# Tempo_viagem_total para HH:MM:SS
tempo_viagem_total_seg = tempo_viagem_total_min * 60
hr_viagem_total = tempo_viagem_total_seg // 3600 # Uma hora tem 3600 segundos.
tempo_viagem_total_seg %= 3600
min_viagem_total = tempo_viagem_total_seg // 60 # Um minuto tem 60 segundos.
tempo_viagem_total_seg %= 60
seg_viagem_total = tempo_viagem_total_seg

# Tempo_em_movimento_total para HH:MM:SS
tempo_movi_total_seg = tempo_movi_total_min * 60
hr_movi_total = tempo_movi_total_seg // 3600
tempo_movi_total_seg %= 3600
min_movi_total = tempo_movi_total_seg // 60
tempo_movi_total_seg %= 60
seg_movi_total = tempo_movi_total_seg

# Resultados da viagem
print('Dados do computador de bordo:')
print(f'O tempo de viagem (no formato HH:MM:SS):{hr_viagem_total:02d}:{min_viagem_total:02d}:{seg_viagem_total:02d}')
print(f'O tempo em movimento da viagem (no formato HH:MM:SS):{hr_movi_total:02d}:{min_movi_total:02d}:{seg_movi_total:02d}')
print(f'A velocidade média da viagem (Km/h):{vel_media_viagem:.2f}km/h e a velocidade média em movimento (Km/h):{vel_media_movi:.2f}km/h')
print(f'O custo do cosbustível da viagem:R${custo_total_viagem:.2f}')
print('Dados do desempenho do veículo durante a viagem:')
print(f'O desempenho do carro (em Km/l, l/h e R$/Km):{desempenho_em_km_l:.2f}km/l, {comb_litros_por_h:.2f}l/h e {custo_por_km:.2f}R$/km')