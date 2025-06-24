'''Um determinado material radioativo perde metade de sua massa a cada 50 segundos. 
Faça um programa que solicite a massa inicial (em gramas) e que calcule o tempo necessário 
para que essa massa se torne menor que 0,5 grama. Ao término, o programa deve exibir a massa inicial, 
a massa final e o tempo que levou para o decaimento (exiba o tempo informando horas, minutos e segundos).

Exemplo de saída:
Massa Inicial: 250 gramas
Massa Final: 0.48828125 gramas
Tempo de Decaimento: 0:07:30'''

import sys

# Solicitar a massa do material
try:
    massa_inicial = float(input('Digite o valor da massa inicial (em gramas): '))
    if massa_inicial <= 0:
        sys.exit('Digite um valor positivo!')
except ValueError:
    sys.exit('Informe apenas valores reais para a massa do material que vai sofrer decaimento.')
except Exception as e:
    sys.exit(f'ERRO: {e}')

# Definindo as variáveis.
else:
    tempo_total = 0
    massa_decaimento = massa_inicial

while massa_decaimento >= 0.5:
    massa_decaimento /= 2 # dividir a massa pela metade ( meia vida ).
    tempo_total = tempo_total + 50 # adicionar 50 segundos ao tempo total.

# Definindo a variável da massa pós decaimento.
massa_final = massa_decaimento

# Convertendo o tempo total ( segundos ) para o formato HH:MM:SS.
horas = tempo_total // 3600
tempo_total %= 3600
minutos = tempo_total // 60
tempo_total %= 60
segundos = tempo_total

print(f'Massa inicial ( em gramas ):{massa_inicial:.2f} gramas.')
print(f'Massa final ( em gramas ): {massa_final:.2f} gramas.')
print(f'Tempo total de decaimento: {horas:02d}h:{minutos:02d}min:{segundos:02d}seg')






