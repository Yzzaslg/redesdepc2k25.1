'''Em um estacionamento, as tarifas são as seguintes (cumulativas):

Até duas horas: R$ 8,00/hora ou fração;
Entre três e quatro horas: R$ 5,00/hora ou fração;
Horas seguintes: R$ 3,00/hora ou fração;
Depois de 12h, o custo passa a ser fixo: R$ 30,00.

Faça um programa que solicite ao usuário o tempo que um veículo permaneceu no 
estacionamento (no formato HH:MM) e exiba o valor a ser pago pelo responsável.

Como exemplo, considere que o carro ficou 5 horas e 10 minutos no estacionamento; 
deve pagar: R$ 16,00 (pelas duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) 
+ R$ 6,00 (pela quinta hora e fração da sexta hora): total de R$ 32,00'''

import sys

# Solicitando dados ao usuário
try:
    print('Informe o tempo que o veículo permaneceu no estacionamento em HH:MM:')
    horas = int(input('Digite as horas ( de 0h a 23h): '))
    if horas < 0 or horas > 23:
        sys.exit('Digite um valor entre 0 e 23 para as horas.')
    minutos = int(input('Digite os minutos ( de 0min a 59min ): '))
    if minutos < 0 or minutos > 59:
        sys.exit('Digite um valor entre 0 e 59 para os minutos.')

except ValueError:
    sys.exit('Informe valores inteiros para horas e minutos.')

print(f'Tempo de permanência no estacionamento:{horas:02d}h e {minutos:02d}min')

# Convertendo horas em minutos
total_minutos = horas * 60 + minutos

# Condições de valores
# valor de 12h = 720 minutos é fixo em R$ 30,00.
if total_minutos > 720:
    valor = 30.00

# Valores em horas ( convertendo minutos em horas )
else:
    total_horas = total_minutos // 60
    if total_minutos % 60 != 0:
        total_horas = total_horas + 1

# Calculo dos valores por horas
if total_horas <= 2:
    valor = total_horas * 8
elif total_horas <= 4:
    valor = 2 * 8 + ( total_horas - 2 ) * 5 # primeiras 2 horas + o que ele vai passar...
else:
    valor = 2 * 8 + 2 * 5 + ( total_horas - 4 ) * 3 # primeiras 4 horas + o que ele vai passar...

# Calculo do valor final que o veiculo permaneceu no estacionamento
print(f'Valor do tempo permanecido no estacionamento:R${valor:.2f}')