'''O aluno deverá implementar um programa em Python para simular a movimentação de um robô em um plano cartesiano.

Requisitos do sistema:

1. O programa deve solicitar ao usuário:
i. A posição inicial do robô, informando as coordenadas X e Y;
ii. A sequência de movimentos que o robô deve executar;

2. O programa deve:
i. Calcular a posição final do robô após executar os movimentos válidos;
ii. Determinar em qual quadrante (ou eixo/origem) o robô se encontra antes e depois da movimentação;
iii. Exibir as seguintes informações:
    º Posição inicial e seu respectivo quadrante;
    º Lista de movimentos válidos realizados e a quantidade deles;
    º Posição final e seu respectivo quadrante.

3. A funções devem validar as entradas e tratar possíveis erros, como:
i. Coordenadas não numéricas (INT ou FLOAT);
ii. Movimentos inválidos;
iii. Tipos de dados incompatíveis para as funções.
'''

import sys
from robo_funcoes import quadrante, movimenta

# Solicitar as posições iniciais ao usuário.
try:
    x_i = int(input('Dgite um valor para a posição X inicial: '))
    y_i = int(input('Dgite um valor para a posição Y inicial: '))
except ValueError:
    sys.exit('Valor inválido, por favor digite valores inteiros para X e Y...')
except Exception as e:
    sys.exit(f'ERR0: {e}')

# String de comandos.
comandos = input('Digite os comandos de movimentos do robô (U, D, R, L, O, N, E e W) : ')
comandos = comandos.upper() # Converter para maiúsculo como padrão.
if comandos.strip() == '': # caso o usuário digite apenas espaço e der enter, strip retorna uma string vazia inválida para os movimentos.
    sys.exit('Nenhum comando foi digitado, o robô não vai se mover...')

# Registrar a movimentação do robô.
posicao_i, movimentos_validos, movimentos_invalidos, movimentos, posicao = movimenta((x_i, y_i), comandos)

# Determinar o quadrante inicial e final.
posicao_inicial, quadrante_inicial = quadrante(posicao_i)
posicao_final, quadrante_final = quadrante(posicao)

# Resultados.
print('--- Resultados: ---')
print(f'\nPosição inicial do robô: ({x_i},{y_i}) ')
print(f'Posição final do robô: {posicao_final}')
print(f'Quantidade de movimentos efetuados: {movimentos}')
print(f'Movimentos efetuados: {movimentos_validos}')
print(f'Letras inválidas para os movimentos:{movimentos_invalidos}')
print(f'Quadrante inicial: {quadrante_inicial}')
print(f'Quadrante final: {quadrante_final}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')

